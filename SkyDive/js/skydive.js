$(function() {
  var app = {};
  app.constants = {};
  app.controlFlag = {};

  app.constants.NB_IMAGES = 2;
  app.controlFlag.imagesLoaded = 0;

  //this is the JQuery object (DOM + CSS + helpers)
  app.renderedCanvas = $("#skydive");
  //this is the raw DOM element
  app.canvas = app.renderedCanvas.get(0);
  if (initGL(app)) {
    initShaders(app);
    initBuffers(app);
    initTextures(app);

    app.gl.clearColor(0.0, 1.0, 1.0, 1.0);
    app.gl.enable(app.gl.DEPTH_TEST);

    //Initializes the scene object
    app.scene = {};
    setupAnimation(app);

    //Launches the frame rendering loop
    new MyAnimation(app);
  }
});

function setupAnimation(app) {
  app.animation = {};
  app.animation.distanceFallen = 0;
  app.animation.lastRendering = new Date().getTime();
  app.animation.totalDistanceFallen = 0;

  app.constants.jumpHeight = 4000;
  app.constants.fallSpeed = 600;
}

function initGL(app) {
  app.gl = WebGLUtils.setupWebGL(app.canvas);
  if ( !app.gl ) {
    alert("Your browser does not seem to support webGL, sorry");
    return false;
  }

  //the WebGL content is actually rendered in the canvas DOM element, BEFORE
  //it is "transformed" by the CSS.
  //While there is a couple of things you can do by having you canvas size and
  //your CSS size different, here I prefer to force them to the same and control
  //my canvas size through the CSS.
  app.canvas.width = app.renderedCanvas.width();
  app.canvas.height = app.renderedCanvas.height();

  app.gl.viewportWidth = app.canvas.width;
  app.gl.viewportHeight = app.canvas.height;

  return true;
}

function initShaders(app) {
  //Gets the shaders from the DOM
  var fragmentShader = getShader(app.gl, "shader-fs");
  var vertexShader = getShader(app.gl, "shader-vs");

  //Attaches the shaders to the WebGL object
  app.gl.shaderProgram = app.gl.createProgram();
  app.gl.attachShader(app.gl.shaderProgram, vertexShader);
  app.gl.attachShader(app.gl.shaderProgram, fragmentShader);
  app.gl.linkProgram(app.gl.shaderProgram);

  if (!app.gl.getProgramParameter(app.gl.shaderProgram, app.gl.LINK_STATUS)) {
    alert("Could not initialise shaders");
  }

  //Make the program the active one
  app.gl.useProgram(app.gl.shaderProgram);

  //Retrieves the attributes and the uniforms pointers.
  app.gl.shaderProgram.vertexPositionAttribute = app.gl.getAttribLocation(app.gl.shaderProgram, "aVertexPosition");
  app.gl.enableVertexAttribArray(app.gl.shaderProgram.vertexPositionAttribute);

  app.gl.shaderProgram.vertexTextureAttribute = app.gl.getAttribLocation(app.gl.shaderProgram, "aTextureCoord");
  app.gl.enableVertexAttribArray(app.gl.shaderProgram.vertexTextureAttribute);

  app.gl.shaderProgram.pMatrixUniform = app.gl.getUniformLocation(app.gl.shaderProgram, "uPMatrix");
  app.gl.shaderProgram.mvMatrixUniform = app.gl.getUniformLocation(app.gl.shaderProgram, "uMVMatrix");
  app.gl.shaderProgram.uSampler = app.gl.getUniformLocation(app.gl.shaderProgram, "uSampler");
}

function initTextures(app) {
  app.textures = {};

  app.textures.corbas = app.gl.createTexture();
  app.textures.corbas.image = new Image();
  //Creates a callback to be sure that the GL binding happens AFTER the image
  //is loaded
  app.textures.corbas.image.onload = function () {
    handleLoadedTexture(app, app.textures.corbas);
  };
  app.textures.corbas.image.src = "resources/Corbas-512-gmaps_scale500m.gif";

  app.textures.splash = app.gl.createTexture();
  app.textures.splash.image = new Image();
  app.textures.splash.image.onload = function () {
    handleLoadedTexture(app, app.textures.splash);
  };
  app.textures.splash.image.src = "resources/splash.gif";
}

function allImageLoaded(app) {
  return app.controlFlag.imagesLoaded === app.constants.NB_IMAGES;
}

//Callback on the image load that binds the texture to gl
function handleLoadedTexture(app, texture) {
  app.controlFlag.imagesLoaded = app.controlFlag.imagesLoaded + 1;

  app.gl.bindTexture(app.gl.TEXTURE_2D, texture);
  app.gl.pixelStorei(app.gl.UNPACK_FLIP_Y_WEBGL, true);
  app.gl.texImage2D(app.gl.TEXTURE_2D, 0, app.gl.RGBA, app.gl.RGBA, app.gl.UNSIGNED_BYTE, texture.image);
  app.gl.texParameteri(app.gl.TEXTURE_2D, app.gl.TEXTURE_MAG_FILTER, app.gl.NEAREST);
  app.gl.texParameteri(app.gl.TEXTURE_2D, app.gl.TEXTURE_MIN_FILTER, app.gl.NEAREST);
  app.gl.bindTexture(app.gl.TEXTURE_2D, null);
}

function initBuffers(app) {
  app.buffers = {};
  app.buffers.squareVertexPositionBuffer = app.gl.createBuffer();
  app.gl.bindBuffer(app.gl.ARRAY_BUFFER, app.buffers.squareVertexPositionBuffer);
  vertices = [
    1250.0,  1250.0,  0.0,
    -1250.0,  1250.0,  0.0,
    1250.0, -1250.0,  0.0,
    -1250.0, -1250.0,  0.0
      ];
  app.gl.bufferData(app.gl.ARRAY_BUFFER, new Float32Array(vertices), app.gl.STATIC_DRAW);
  app.buffers.squareVertexPositionBuffer.itemSize = 3;
  app.buffers.squareVertexPositionBuffer.numItems = 4;

  app.buffers.squareTextureCoordBuffer = app.gl.createBuffer();
  app.gl.bindBuffer(app.gl.ARRAY_BUFFER, app.buffers.squareTextureCoordBuffer);
  texture = [
    1.0, 1.0,
    0.0, 1.0,
    1.0, 0.0,
    0.0, 0.0
    ];
  app.gl.bufferData(app.gl.ARRAY_BUFFER, new Float32Array(texture), app.gl.STATIC_DRAW);
  app.buffers.squareTextureCoordBuffer.itemSize = 2;
  app.buffers.squareTextureCoordBuffer.numItems = 4;
}

// TRICK
// Here we define an object that will be used to store a reference to the app
// context we maintain and that we'll be able to get at each invocation of the
// tick method
//
// Constructor
function MyAnimation(app) {
  this.app = app;
  requestAnimFrame(this.tick.bind(this));
}

MyAnimation.prototype.tick = function(time) {
  this.app.textures.active = this.app.textures.corbas;
  if (allImageLoaded(this.app)) {
    if (this.app.animation.totalDistanceFallen < this.app.constants.jumpHeight) {
      //Queues itself for the next rendering call.
      requestAnimFrame(this.tick.bind(this));
      //renders the frame
      drawscene(this.app);
      //computes the next movement the objects
      animate(this.app);
    } else {
      this.app.textures.active = this.app.textures.splash;
      this.app.animation.distanceFallen = 0;
      drawscene(this.app);
      //Actually asks for the pop-up in the next browser repaint cycle to let
      //the time for the GL to compute the image and the browser to paint it in
      //the canvas
      requestAnimFrame(function () {
        alert("You're dead! What were you waiting for to open your chute?\nOh wait, it's not implemented yet");
      });
    }
  } else {
    //if the images are not yet loaded, just do nothing and loop
    requestAnimFrame(this.tick.bind(this));
  }
};

function drawscene(app) {
  //Defines and clears the GL viewport
  app.gl.viewport(0, 0, app.gl.viewportWidth, app.gl.viewportHeight);
  app.gl.clear(app.gl.COLOR_BUFFER_BIT | app.gl.DEPTH_BUFFER_BIT);

  //Projection matrix
  var pMatrix = mat4.create();
  //Sets the projection matrix
  mat4.perspective(pMatrix, degToRad(45), app.gl.viewportWidth / app.gl.viewportHeight, 0.1, 5000.0);

  //Camera
  var vMatrix = mat4.create();
  mat4.lookAt(vMatrix, [ 0.0,0.0,app.constants.jumpHeight ], [ 0.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ]);

  //Model Matrix
  var mMatrix = mat4.create();
  mat4.translate(mMatrix, mMatrix, [0.0, 0.0, -7.0]);

  var mvMatrix = mat4.create();
  mat4.multiply(mvMatrix, vMatrix, mMatrix);

  //Moves the model by the distance fallen since the last rendering
  mat4.translate(mvMatrix, mvMatrix, [0.0, 0.0, app.animation.distanceFallen]);

  //Links up the buffer data with the attributes (position and color)
  app.gl.bindBuffer(app.gl.ARRAY_BUFFER, app.buffers.squareVertexPositionBuffer);
  app.gl.vertexAttribPointer(app.gl.shaderProgram.vertexPositionAttribute, app.buffers.squareVertexPositionBuffer.itemSize, app.gl.FLOAT, false, 0, 0);

  app.gl.bindBuffer(app.gl.ARRAY_BUFFER, app.buffers.squareTextureCoordBuffer);
  app.gl.vertexAttribPointer(app.gl.shaderProgram.vertexTextureAttribute, app.buffers.squareTextureCoordBuffer.itemSize, app.gl.FLOAT, false, 0, 0);

  if (app.textures.active === app.textures.corbas) {
    app.gl.activeTexture(app.gl.TEXTURE0);
    app.gl.bindTexture(app.gl.TEXTURE_2D, app.textures.corbas);
    app.gl.uniform1i(app.gl.shaderProgram.uSampler, 0);
  } else {
    app.gl.activeTexture(app.gl.TEXTURE1);
    app.gl.bindTexture(app.gl.TEXTURE_2D, app.textures.splash);
    app.gl.uniform1i(app.gl.shaderProgram.uSampler, 1);
  }

  //Links up the matrices data with the uniforms (ModelView and Projection)
  app.gl.uniformMatrix4fv(app.gl.shaderProgram.pMatrixUniform, false, pMatrix);
  app.gl.uniformMatrix4fv(app.gl.shaderProgram.mvMatrixUniform, false, mvMatrix);

  app.gl.drawArrays(app.gl.TRIANGLE_STRIP, 0, app.buffers.squareVertexPositionBuffer.numItems);
}

function animate(app) {
  var timeNow = new Date().getTime();
  var elapsed = timeNow - app.animation.lastRendering;
  app.animation.distanceFallen = app.constants.fallSpeed * elapsed / 1000;
  app.animation.totalDistanceFallen = app.animation.distanceFallen;
}
