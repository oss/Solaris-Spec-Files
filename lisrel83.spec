Summary: confirmatory factor analysis and structural equation modeling
Name: lisrel
Version: 8.3
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
http://www.ssicentral.com/

/usr/local/bin/lisrel83.example is provided as an example of 
how to invoke the program.  

INSTALLATION: (from the vendor README file) 


LISREL 8.30 for SUN is independent of any previous versions.
It means it can coexist w/ previous versions if installed 
in a different directory. The access code schema differs from
previous one. This version contains two additional utilities 
(bin2asc and asc2bin) one can use to convert (LISREL) binary files
to ASCII and viceversa. The installation procedure:

0. save the file in a directory of your choice
1. uncompress lis83aix_bin.tar.Z lis83unix_exp.tar.Z
2. tar -xvf lis*
3. ./lisrel83
4. answer no to the access code question; call or e-mail us the value
listed under ID =
5. w/ the acc. code provided by us, run again LISREL, answer yes and
enter that code.
6. anyone running LISREL, PRELIS or MULTILEVEL programs has to have the 
SSIPATH environment variable set to point to the directory containing 
LICENSE.SSI file. Type:

7' setenv SSIPATH /path/to/lisrel/directory [in a C shell]
7" export SSIPATH=/path/to/lisrel/directory [in a Korn shell]

=================================================================
Scientific Software International, Inc.
7383 N. Lincoln Avenue  Suite 100,  Chicago,  IL 60646-1704,  USA
Tel: (847) 675-0720   Fax: (847) 675-2140   Sales: (800) 247-6113
Web: http://www.ssicentral.com E-Mail: techsupport@ssicentral.com
==================================================================

LICENSE UPDATES: 

Each host that is licensed must have an entry in 
/usr/local/lisrel83/LICENSE.SSI.  An initial version 
is included in the tint package with expiration dates 
at the end of June, 2000.  The presence of this config 
file appears to be all that is required for the 
program to run.  

TESTING LISREL: 

-- Invoke the lisrel program. 

-- The present (broken) version requires the user to have
write access to the directory where the example file is located. 

cp  /usr/local/lisrel83/examples/splex/ex1a.spl /tmp/ex1a.spl 

Input file is:  /tmp/ex1a.spl 

-- Choose an output file name

-- The output should approximate the following (dates, times and CPU 
minutes used will vary): 




                                DATE: 10/21/1999
                                  TIME: 15:23


                                L I S R E L  8.30

                                       BY

                         Karl G. Joreskog & Dag Sorbom



                    This program is published exclusively by
                    Scientific Software International, Inc.
                       7383 N. Lincoln Avenue, Suite 100
                        Chicago, IL 60712-1704, U.S.A.
            Phone: (800)247-6113, (847)675-0720, Fax: (847)675-2140
        Copyright by Scientific Software International, Inc., 1981-99 
          Use of this program is subject to the terms specified in the
                        Universal Copyright Convention.
                          Website: www.ssicentral.com

 The following lines were read from file /tmp/ex1a.spl:

 regression of gnp
 observed variables: gnp labor capital time
 covariance matrix
 4256.530
 449.016     52.984
 1535.097    139.449   1114.447
 537.482     53.291    170.024     73.747
 sample size: 23
 equation:  gnp = labor capital time
 end of problem

 Sample Size =    23

 regression of gnp                                                              

         Covariance Matrix to be Analyzed        

                 gnp      labor    capital       time   
            --------   --------   --------   --------
      gnp    4256.53
    labor     449.02      52.98
  capital    1535.10     139.45    1114.45
     time     537.48      53.29     170.02      73.75
 


 regression of gnp                                                              

 Number of Iterations =  0

 LISREL Estimates (Maximum Likelihood)               
 
      gnp = 3.82*labor + 0.32*capital + 3.79*time, Errorvar.= 12.47, Rý = 1.00
           (0.22)       (0.031)        (0.19)                (4.05)           
            17.70        10.54          20.35                 3.08            
 

         Covariance Matrix of Independent Variables  

               labor    capital       time   
            --------   --------   --------
    labor      52.98
             (17.19)
                3.08
 
  capital     139.45    1114.45
             (64.27)   (361.57)
                2.17       3.08
 
     time      53.29     170.02      73.75
             (18.84)    (76.47)    (23.93)
                2.83       2.22       3.08
 


                           Goodness of Fit Statistics

                              Degrees of Freedom = 0
                 Minimum Fit Function Chi-Square = 0.0 (P = 1.00)
        Normal Theory Weighted Least Squares Chi-Square = 0.00 (P = 1.00)

                  The Model is Saturated, the Fit is Perfect !



          The Problem used     4576 Bytes (=  0.0% of Available Workspace)

                           Time used:    0.043 Seconds

%prep
%setup -q

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

cd $build_dir/files
find . -print | cpio -pdmuv $RPM_BUILD_ROOT

%post
cat <<EOF
http://www.ssicentral.com/

/usr/local/bin/lisrel83.example is provided as an example of 
how to invoke the program.  

INSTALLATION: (from the vendor README file) 


LISREL 8.30 for SUN is independent of any previous versions.
It means it can coexist w/ previous versions if installed 
in a different directory. The access code schema differs from
previous one. This version contains two additional utilities 
(bin2asc and asc2bin) one can use to convert (LISREL) binary files
to ASCII and viceversa. The installation procedure:

0. save the file in a directory of your choice
1. uncompress lis83aix_bin.tar.Z lis83unix_exp.tar.Z
2. tar -xvf lis*
3. ./lisrel83
4. answer no to the access code question; call or e-mail us the value
listed under ID =
5. w/ the acc. code provided by us, run again LISREL, answer yes and
enter that code.
6. anyone running LISREL, PRELIS or MULTILEVEL programs has to have the 
SSIPATH environment variable set to point to the directory containing 
LICENSE.SSI file. Type:

7' setenv SSIPATH /path/to/lisrel/directory [in a C shell]
7" export SSIPATH=/path/to/lisrel/directory [in a Korn shell]

=================================================================
Scientific Software International, Inc.
7383 N. Lincoln Avenue  Suite 100,  Chicago,  IL 60646-1704,  USA
Tel: (847) 675-0720   Fax: (847) 675-2140   Sales: (800) 247-6113
Web: http://www.ssicentral.com E-Mail: techsupport@ssicentral.com
==================================================================

LICENSE UPDATES: 

Each host that is licensed must have an entry in 
/usr/local/lisrel83/LICENSE.SSI.  An initial version 
is included in the tint package with expiration dates 
at the end of June, 2000.  The presence of this config 
file appears to be all that is required for the 
program to run.  

TESTING LISREL: 

-- Invoke the lisrel program. 

-- The present (broken) version requires the user to have
write access to the directory where the example file is located. 

cp  /usr/local/lisrel83/examples/splex/ex1a.spl /tmp/ex1a.spl 

Input file is:  /tmp/ex1a.spl 

-- Choose an output file name

-- The output should approximate the following (dates, times and CPU 
minutes used will vary): 




                                DATE: 10/21/1999
                                  TIME: 15:23


                                L I S R E L  8.30

                                       BY

                         Karl G. Joreskog & Dag Sorbom



                    This program is published exclusively by
                    Scientific Software International, Inc.
                       7383 N. Lincoln Avenue, Suite 100
                        Chicago, IL 60712-1704, U.S.A.
            Phone: (800)247-6113, (847)675-0720, Fax: (847)675-2140
        Copyright by Scientific Software International, Inc., 1981-99 
          Use of this program is subject to the terms specified in the
                        Universal Copyright Convention.
                          Website: www.ssicentral.com

 The following lines were read from file /tmp/ex1a.spl:

 regression of gnp
 observed variables: gnp labor capital time
 covariance matrix
 4256.530
 449.016     52.984
 1535.097    139.449   1114.447
 537.482     53.291    170.024     73.747
 sample size: 23
 equation:  gnp = labor capital time
 end of problem

 Sample Size =    23

 regression of gnp                                                              

         Covariance Matrix to be Analyzed        

                 gnp      labor    capital       time   
            --------   --------   --------   --------
      gnp    4256.53
    labor     449.02      52.98
  capital    1535.10     139.45    1114.45
     time     537.48      53.29     170.02      73.75
 


 regression of gnp                                                              

 Number of Iterations =  0

 LISREL Estimates (Maximum Likelihood)               
 
      gnp = 3.82*labor + 0.32*capital + 3.79*time, Errorvar.= 12.47, Rý = 1.00
           (0.22)       (0.031)        (0.19)                (4.05)           
            17.70        10.54          20.35                 3.08            
 

         Covariance Matrix of Independent Variables  

               labor    capital       time   
            --------   --------   --------
    labor      52.98
             (17.19)
                3.08
 
  capital     139.45    1114.45
             (64.27)   (361.57)
                2.17       3.08
 
     time      53.29     170.02      73.75
             (18.84)    (76.47)    (23.93)
                2.83       2.22       3.08
 


                           Goodness of Fit Statistics

                              Degrees of Freedom = 0
                 Minimum Fit Function Chi-Square = 0.0 (P = 1.00)
        Normal Theory Weighted Least Squares Chi-Square = 0.00 (P = 1.00)

                  The Model is Saturated, the Fit is Perfect !



          The Problem used     4576 Bytes (=  0.0% of Available Workspace)

                           Time used:    0.043 Seconds
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/lisrel83
