;;; START THE DATA DEFINITION

(defparameter *nodes* '((living-room (you are in the living room.
                          a wizard is snoring loudly on the couch.))
                        (garden (you are in a beautiful garden.
                          there is a well in front of you.))
                        (attic (you are in the attic.
                          there is a giant welding torch in the corner.))))

(defparameter *edges* '((living-room (garden west door)
                                     (attic upstairs ladder))
                        (garden (living-room east door))
                        (attic (living-room downstairs ladder))))

(defparameter *objects* '(whiskey bucket frog chain))

(defparameter *object-location* '((whiskey living-room)
                                  (bucket living-room)
                                  (frog garden)
                                  (chain garden)))

(defparameter *location* 'living-room)

(defparameter *allowed-commands* '(look walk pickup inventory))

;;; STOP THE DATA DEFINITION
;;; START THE LOGIC DEFINITION

(defun describe-location (location nodes)
  (cadr (assoc location nodes)))

(defun describe-path (edge)
  `(there is a ,(caddr edge) going ,(cadr edge) from here.))

(defun describe-paths (location edges)
  (apply #'append (mapcar #'describe-path (cdr (assoc location edges)))))

(defun objects-at (loc objs obj-loc)
  (labels ((at-loc-p (objs)
              (eq (cadr (assoc objs obj-loc)) loc)))
    (remove-if-not #'at-loc-p objs)))

(defun describe-objects (loc objs obj-loc)
  (labels ((describe-obj (obj)
              `(you see a ,obj on the floor.)))
    (apply #'append (mapcar #'describe-obj (objects-at loc objs obj-loc)))))

;;; STOP LOGIC DEFINITION
;;; START USER ACTIONS

(defun look ()
  (append (describe-location *location* *nodes*)
          (describe-paths *location* *edges*)
          (describe-objects *location* *objects* *object-location*)))

(defun walk (direction)
  (let ((next (find direction
                    (cdr (assoc *location* *edges*))
                    :key #'cadr)))
    (if next
      (progn (setf *location* (car next))
             (look))
      '(you cannot go that way))))

(defun pickup (object)
  (cond ((member object
                 (objects-at *location* *objects* *object-location*))
         (push (list object 'body) *object-location*)
         `(you are now carrying the ,object))
        (t '(you cannot get that.))))

(defun inventory ()
  (cons 'items- (objects-at 'body *objects* *object-location*)))

;;; STOP USER ACTIONS
;;; START USER INTERFACE
(defun say-hello ()
  (princ "Please enter your name:")
  (let ((name (read-line)))
    (princ "Nice to meet you, ")
r   (princ name)))

(defun game-repl ()
  (let ((cmd (game-read)))
    (unless (eq (car cmd) 'quit)
      (game-print (game-eval cmd))
      (game-repl))))

(defun game-read ()
  (let ((cmd (read-from-string
               (concatenate 'string "(" (read-line) ")"))))
    (flet ((quote-it (x)
                     (list 'quote x)))
      (cons (car cmd) (mapcar #'quote-it (cdr cmd))))))

(defun game-eval (exp)
  (if (member (car exp) *allowed-commands*)
    (eval exp)
    '(I do not know that command)))

(defun tweak-text (lst caps lit)
  (when lst
    (let ((item (car lst))
          (rest (cdr lst)))
      (cond ((eql item #\space) (cons item (tweak-text rest caps lit)))
            ((member item '(#\! #\? #\.)) (cons item (tweak-text rest t lit)))
            ((eql item #\") (tweak-text rest caps (not lit)))
            (lit (cons item (tweak-text rest nil lit)))
            (caps (cons (char-upcase item) (tweak-text rest nil lit)))
            (t (cons (char-downcase item) (tweak-text rest nil nil)))))))

(defun game-print (lst)
  (princ (coerce (tweak-text (coerce (string-trim "() "
                                                  (prin1-to-string lst))
                                     'list)
                             t
                             nil)
                 'string))
  (fresh-line))
;;; STOP USER INTERFACE
