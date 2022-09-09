Lemma ex1: forall A, ~~~A -> ~A.
Proof.
intro h1.
intro h2.
intro h3.
destruct h2.
intro h4.
destruct h4.
assumption.
Qed.

Lemma ex2: forall A B, A \/ B -> ~ (~A /\ ~B).
Proof.
intro h1.
intro h2.
intro h3.
intro h4.
destruct h4 as (l1,m2).
destruct h3 as [l2|l2].
destruct l1.
assumption.
destruct m2.
assumption.
Qed.

Lemma ex3: forall T (P:T -> Prop),
(~ exists x, P x) -> forall x, ~ P x.
Proof.
intro h1.
intro h2.
intro h3.
intro h4.
intro h5.
destruct h3.
exists h4.
assumption.
Qed.