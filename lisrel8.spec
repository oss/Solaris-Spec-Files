Summary: confirmatory factor analysis and structural equation modeling
Name: lisrel
Version: 8
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
Comments:

http://www.ssicentral.com/

INSTALLATION: 

-- Install the package. 

-- At the end of the installation: 

cd /usr/local/lisrel
./update 

RECOMMENDED LINKS: 

ln -s /usr/local/lisrel/lisrel8  /usr/local/bin/lisrel8
ln -s /usr/local/lisrel/prelis2 /usr/local/bin/prelis2

LICENSE UPDATES: 

Each host that is licensed must have an entry in /usr/local/lisrel/config.c. 
The entry consists of the hostid.  Also required is a special vendor 
access code.  

Should the contents of config.c change (that is, should a host be
added or removed), the file config.c needs to be modified accordingly
and the script /usr/local/lisrel/update run again. The config.c 
file is the same on each system and must include all of the hostids
that are valid at Rutgers.  Hence, the file is included as part of this
package. 

When the "update" script is run, the files 

prelis2
config.o 
lisrel8 

are updated.  Permissions on prelis2 and lisrel8 then need to be 
corrected to 755, as the script modifies them.  

TESTING LISREL: 

-- Invoke 

		lisrel8 

-- Input file name is: 

	 /usr/local/lisrel/examples/splex/ex1a.spl

-- Choose an output file name

-- The output should approximate the following (dates, times and CPU 
minutes used will vary): 





                  This copy authorized for use on  16 node(s).
                        UNTIL MONTH/DAY/YEAR = 12/31/99


                              DATE:  8/25/99

                              TIME: 19: 1:26

                         SUN/SOLARIS 2  L I S R E L  8.11

                                       BY

                         KARL G JORESKOG AND DAG SORBOM



                    This program is published exclusively by
                    Scientific Software International, Inc.
                       1525 East 53rd Street - Suite 530
                        Chicago, Illinois 60615, U.S.A.
               Voice: (800)247-6113, (312) 684-4920 Fax: (312)684-4979
        Copyright by Scientific Software International, Inc., 1981-94.
         Partial copyright by SUN Microsystem Inc., 1993.
          Use of this program is subject to the terms specified in the
                        Universal Copyright Convention.

 The following lines were read from file
/usr/local/lisrel/examples/splex/ex1a.spl



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

         COVARIANCE MATRIX TO BE ANALYZED

                 gnp      labor    capital       time
            --------   --------   --------   --------
      gnp    4256.53
    labor     449.02      52.98
  capital    1535.10     139.45    1114.45
     time     537.48      53.29     170.02      73.75



 regression of gnp
 Number of Iterations =  0

 LISREL ESTIMATES (MAXIMUM LIKELIHOOD)

      gnp = 3.82*labor + 0.32*capital + 3.79*time, Errorvar.= 12.47, R* = 1.00
           (0.22)       (0.031)        (0.19)                (4.05)
            17.70        10.54          20.35                 3.08



         COVARIANCE MATRIX OF INDEPENDENT VARIABLES

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



                           GOODNESS OF FIT STATISTICS

               CHI-SQUARE WITH 0 DEGREE OF FREEDOM = 0.0 (P = 1.00)

                  The Model is Saturated, the Fit is Perfect !



          THE PROBLEM USED     4008 BYTES (=  0.4% OF AVAILABLE WORKSPACE)

                           TIME USED:     1.0 SECONDS

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
Comments:

http://www.ssicentral.com/

INSTALLATION: 

-- Install the package. 

-- At the end of the installation: 

cd /usr/local/lisrel
./update 

RECOMMENDED LINKS: 

ln -s /usr/local/lisrel/lisrel8  /usr/local/bin/lisrel8
ln -s /usr/local/lisrel/prelis2 /usr/local/bin/prelis2

LICENSE UPDATES: 

Each host that is licensed must have an entry in /usr/local/lisrel/config.c. 
The entry consists of the hostid.  Also required is a special vendor 
access code.  

Should the contents of config.c change (that is, should a host be
added or removed), the file config.c needs to be modified accordingly
and the script /usr/local/lisrel/update run again. The config.c 
file is the same on each system and must include all of the hostids
that are valid at Rutgers.  Hence, the file is included as part of this
package. 

When the "update" script is run, the files 

prelis2
config.o 
lisrel8 

are updated.  Permissions on prelis2 and lisrel8 then need to be 
corrected to 755, as the script modifies them.  

TESTING LISREL: 

-- Invoke 

		lisrel8 

-- Input file name is: 

	 /usr/local/lisrel/examples/splex/ex1a.spl

-- Choose an output file name

-- The output should approximate the following (dates, times and CPU 
minutes used will vary): 





                  This copy authorized for use on  16 node(s).
                        UNTIL MONTH/DAY/YEAR = 12/31/99


                              DATE:  8/25/99

                              TIME: 19: 1:26

                         SUN/SOLARIS 2  L I S R E L  8.11

                                       BY

                         KARL G JORESKOG AND DAG SORBOM



                    This program is published exclusively by
                    Scientific Software International, Inc.
                       1525 East 53rd Street - Suite 530
                        Chicago, Illinois 60615, U.S.A.
               Voice: (800)247-6113, (312) 684-4920 Fax: (312)684-4979
        Copyright by Scientific Software International, Inc., 1981-94.
         Partial copyright by SUN Microsystem Inc., 1993.
          Use of this program is subject to the terms specified in the
                        Universal Copyright Convention.

 The following lines were read from file
/usr/local/lisrel/examples/splex/ex1a.spl



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

         COVARIANCE MATRIX TO BE ANALYZED

                 gnp      labor    capital       time
            --------   --------   --------   --------
      gnp    4256.53
    labor     449.02      52.98
  capital    1535.10     139.45    1114.45
     time     537.48      53.29     170.02      73.75



 regression of gnp
 Number of Iterations =  0

 LISREL ESTIMATES (MAXIMUM LIKELIHOOD)

      gnp = 3.82*labor + 0.32*capital + 3.79*time, Errorvar.= 12.47, R* = 1.00
           (0.22)       (0.031)        (0.19)                (4.05)
            17.70        10.54          20.35                 3.08



         COVARIANCE MATRIX OF INDEPENDENT VARIABLES

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



                           GOODNESS OF FIT STATISTICS

               CHI-SQUARE WITH 0 DEGREE OF FREEDOM = 0.0 (P = 1.00)

                  The Model is Saturated, the Fit is Perfect !



          THE PROBLEM USED     4008 BYTES (=  0.4% OF AVAILABLE WORKSPACE)

                           TIME USED:     1.0 SECONDS

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/man/man1/*
/usr/local/lisrel
