600

halfdt3 new $1=(n\_half\_$ product3newl* $p\_half\_$ roduct3newl+ $n\_half\_product3\_ex*p\_half\_product3\_ex)$ 

$1$ $(n\_half\_product3\_new1+n\_half\_$ product3ex

600

nhalfproduct3new $1=n\_half\_product3\_$ $\_newl+n\_half\_product3\_ex$ 

610

＃todo：半成品拆成零件（仅拆前方留下半成品次品）

611

npartlnew1, $n\_part2\_new1$  $n\_part3\_new1$  Ppart1newl,ppart2new1, ppart3new $1=$ 

612

dealproductbad3(nhalfproduct1ex2 * phalfproduct1dismantle,

613

[ppartlmake, ppartlmake,ppartlmake],

$p\_half\_$ product1make)

614

npart4new1, npart5new1,npart6newl,ppart4newl,ppart5new1, $P\_part6\_$ new1 $=$ 

615

dealproductbad3(nhalfproduct2 $t2\_ex2*$ phalfproduct2dismantle,

616

[ppart4make,ppart5make,ppart6make],

phalfproduct2make)

617

npart7newl,npart8new1,ppart7newl, $\text {p_{part}8_{new}1=}$ 

618

$deal\_product\_bad2(n\_half\_product3\_ex2*p\_half\_product3\_dismantle$ ,[ppart7make, $p\_part8\_make],$ 

619

phalfproduct3make)

620

＃ todo：计算半成品拆解费

621

W $\_1\_new$ $-=n\_part1\_$ newl * mhalfproductldismantle $+n\_part4$ new1* $m\_half$ product2dismantle +npart7newl *mhalfproduct3dismantle

023

＃todo：得到当前零件数，得到当前零件次品率

623

if $n\_part1\_new1+n\_part1\_ex1=0:$ 

624

$$\text {P_{part}1_{new}1=}0$$

625

$$\text {n_{part}1_{new}1=}0$$

626

else:

627

$p\_part1\_new1=(n\_part1\_new1*p\_part1\_new1+n\_part1\_ex1*p\_part1\_ex)$ /( $n\_part1\_new1+n\_part1\_ex1)$ 

020

$$n\_partl\_newl=n\_partl\_newl+n\_partl\_exl$$

629

if $n\_part2\_new1+n\_part2\_ex1=0:$ 

630

$$\text {p_{part}2_{new}1=0}$$

631

$$\text {n_{part}2_{new}1=0}$$

631

else:

633

$p\_part2\_new1=(n\_part2\_new1*p\_part2\_new1+n\_part2\_ex1*p\_part2\_ex)$ /( $n\_part2\_new1+n\_part2\_ex1)$ 

634

$$\text {n_{part}2_{new}1=n_{part}2_{new}1+n_{part}2_{ex1}}$$

635

if $n\_part3\_new1+n\_part3\_ex1=0:$ 

636

$$\text {p_{part}3_{new}1=0}$$

637

$$\text {n_{part}3_{new}1=0}$$

030

else:

639

$$p\_part3\_new1=(n\_part3\_new1*p\_part3\_new1+n\_part3\_ex1*p\_part3\_ex)/(\quad n\_part3\_new1+n\_part3\_ex1)$$

640

$$\text {n_{part}3_{new}1=n_{part}3_{new}1+n_{part}3_{ex1}}$$

641

if $n\_part4\_new1+n\_part4\_ex1=0:$ 

642

$$\text {P_{part}4_{new}1=0}$$

643

$$\text {n_{part}4_{new}1=0}$$

644

else:

645

640

$$\text {n_{part}4_{new}1=n_{part}4_{new}1+n_{part}4_{ex1}}$$

$p\_part4\_new1=(n\_part4\_new1*p\_part4\_new1+n\_part4$ $ext.ppartaex)$ /( $\text {n_{part}4_{new}1+n_{part}4_{ex}1)}$ $dsmo$ 

<!-- 66 -->

