# A sharp mixed-decoder operator envelope

Reviewed main: `ef3a6c9f62f7b9b591b56503ba5d24e0b10d2c12` (PR #24).
Date: 2026-09-23. Status: derived and independently reconstructed within
the workspace. This improves the core decoder classification threshold;
it excludes no new entropy states by itself. It accompanies the
[parity continuation](PARITY_READOUT_BOUND.md).

For a three-qubit state on A,B,M, consider a score with two traceless qubit decoders at A and one scalar/one traceless decoder at B. Absorb signs and interchange B's X/Z queries if needed:

 H = X_A (n dot sigma_M) + Z_A (k dot sigma_M) + X_B + Z_B (N dot sigma_M),

with unit n,k,N. The claim is

 ||H|| <= max_{0<=a<=1} [sqrt(2-a^2)+sqrt(a^2+2a+2)]
        < sqrt(21/2) < 13/4 < 10/3.

The strict first comparison follows because equality in weighted Cauchy below would require a=1 and sqrt(5)=2 simultaneously. The numerical sharp constant is about 3.2391658042, but no decimal is needed for the clean sqrt(21/2) upper bound.

## 1. Canonical active pair

The directions n+k and n-k are orthogonal. Rotate the A and M coordinates to put

 H = a X_A X_M + b Z_A Z_M + X_B + Z_B N_M,
 a,b>=0, a^2+b^2=2, a<=b.

This is a coordinate change in a proof about the given observables; it does not alter the operational query set. Thus 0<=a<=1. Write N=n_x X+n_y Y+n_z Z.

Direct Pauli multiplication gives

 H^2 = 4 I - 2ab Y_A Y_M
       +2 X_B(a X_A X_M+b Z_A Z_M)
       +2 Z_B(a n_x X_A+b n_z Z_A).

In particular H^2 is affine in (n_x,n_z) and independent of n_y. Convexity of the largest eigenvalue on the closed unit disk shows its maximum is achieved on the boundary. It therefore suffices to put N=x X+z Z with x^2+z^2=1.

## 2. Two-qubit representation of H^2

Set K=(H^2-4I)/2 and

 B=X_A X_B X_M, C=Z_A X_B Z_M,
 D=X_A Z_B, E=Z_A Z_B.

Then BC=-Y_A Y_M. The Pauli pairs (B,D) and (C,BE) anticommute internally and commute across pairs. Hence their algebra is the standard two-qubit Pauli algebra with multiplicity two; choose

 B=Z_1, D=X_1, C=Z_2, BE=X_2.

Consequently the eigenvalues of K, each repeated twice, are those of

 K_4=ab Z_1 Z_2+a Z_1+b Z_2+a x X_1+b z Z_1 X_2.

Let v=x^2. Its characteristic polynomial is

 D(lambda,v) = [lambda^2-a^2(1+b^2)+(b^2-a^2)v]^2
               -4b^2(lambda+a^2)^2
               +4b^2(b^2-a^2)(1-v).

For a direct derivation use the Z_1 block matrix. Its diagonal blocks are

 A=aI+b(1+a)Z+bzX,
 C=-aI+b(1-a)Z-bzX,

and its off-diagonal block is ax I. Thus the determinant equals

 det[(lambda I-A)(lambda I-C)-a^2x^2 I].

Writing the 2x2 matrix in Pauli coordinates yields exactly D above. The block determinant identity extends by polynomial continuity if one of the diagonal blocks is singular.

## 3. A principal axis maximizes the norm

At v=0, the largest eigenvalue of K_4 is

 lambda_0=a+b sqrt(a^2+2a+2).

This also follows directly from the original Hamiltonian at N=Z: Z_A Z_M commutes with H, and the remaining commuting product X_A X_B X_M splits H into two-dimensional sectors. Its norm is

 f(a)=b+sqrt((a+1)^2+1),

and (f(a)^2-4)/2=lambda_0.

Put h=lambda^2-a^2(1+b^2)+(b^2-a^2)v. Differentiation gives

 partial_v D = 2(b^2-a^2)(h-2b^2).

For every lambda>=lambda_0 and v>=0,

 h-2b^2 >= lambda_0^2-a^2(1+b^2)-2b^2
          =2ab[sqrt(a^2+2a+2)+b] >=0.

Thus D(lambda,v)>=D(lambda,0)>0 for every lambda>lambda_0. The final strict positivity holds because lambda_0 is the largest eigenvalue of K_4 at v=0. Hence K_4 has no eigenvalue above lambda_0 at any v in [0,1]. This proves ||H||<=f(a), with equality at N=Z. No optimization over a has been used in this step.

## 4. A simple uniform constant

Weighted Cauchy (u+v)^2<=3u^2+(3/2)v^2 gives

 f(a)^2 <=3(2-a^2)+(3/2)(a^2+2a+2)
         =21/2-(3/2)(a-1)^2 <=21/2.

Therefore every such mixed inactive decoder pattern has score strictly below sqrt(21/2). A rank-two core whose score exceeds sqrt(21/2) necessarily has exactly one active site and two scalar decoders at its inactive site. The zero/two-active cases are already bounded by 2sqrt(2) via the established rank-two monogamy argument.

This replaces the older 10/3 sufficient classification threshold. Extending the subsequent principal-angle/certified tail analysis to this larger core set requires additional work; the threshold alone does not prove the missing entropy inequality.

## 5. Verification and remaining novelty boundary

Small 8x8 exploratory calculations motivated the bound. They are not the
proof. Another agent independently reconstructed the canonicalization,
Pauli representation, characteristic polynomial and orientation comparison.
The standard-library exact checker
[check_parity_and_decoder.py](../../tools/check_parity_and_decoder.py)
expands the 4x4 determinant directly by its 24 permutation terms, checks
the derivative and endpoint polynomial identities, and verifies the scalar
comparisons. It does not certify the later tail argument or originality.

The sharp scalar maximum occurs at a unique interior point: the second
derivative of f is `-2/b^3+1/[(a+1)^2+1]^(3/2)<0`, while f' is positive
at zero and negative at one. Its stationary equation is

 2a^4+4a^3+a^2-4a-2=0.

The zero/two-active decoder cases use the established Cheng–Hall monogamy
input in the [rank-two proof](../ENTROPY_INEQUALITY_BOUNDARIES.md).
This mixed pattern is a separate finite-dimensional operator calculation.
Its particular sharp envelope has not received a completed primary-source
subsumption comparison; publication originality remains unresolved.
The note preserves arbitrary complex decoder directions and the original
single-query model. No simultaneous execution of the four decoders or
restriction of the physical encoder is assumed.
