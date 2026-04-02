(define (ascending? s)
  (cond 
    ((null? s)
     #t)
    ((null? (cdr s))
     #t)
    (else
     (if (<= (car s) (car (cdr s)))
         (ascending? (cdr s))
         #f))))

(define (my-filter pred s)
  (if (null? s)
      ()
      (if (pred (car s))
          (cons (car s) (my-filter pred (cdr s)))
          (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1)
     lst2)
    ((null? lst2)
     lst1)
    ((cons (car lst1)
           (cons (car lst2)
                 (interleave (cdr lst1) (cdr lst2)))))))

(define (no-repeats s)
    (if 
        (null? s)
        '()
         (cons
             (car s)
             (no-repeats
                 (my-filter 
                        (lambda (x) (not (= x (car s))))
                        s)))
                            ))