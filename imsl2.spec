Summary: IMSL math library
Name: imsl
Version: 2.1
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
http://www.vni.com/products/imsl/

The file /usr/local/vni2.1/license/license.dat is a configuration file,
and is in the configuration server.  The Rutgers license number 
is 606926.  

The IMSL MATH/LIBRARY is a collection of FORTRAN routines and
functions useful in research and mathematical analysis. Each routine
is designed and documented to be used in research activities as well
as by technical specialists. To use any of these routines, you must
write a program in FORTRAN (or possibly some other language) to call
the MATH/LIBRARY routine. 

NB: You must have Fortran installed. 

See Installation_Notes in this directory for environment variables
recommended by the vendor.  

INSTALLATION: 

-- Install the rpm package. 

-- After the software has been copied to your system, connect to the
/usr/local/vni2.1 directory.  The next several steps are to validate
that it is working properly.  

-- Start a Bourne shell. 

.  ./CTT2.1/ctt/bin/cttsetup.sh

Note: This sets environment variables that are useful later

cd $CTT_EXAMPLES/f90/validate
$F90 $F90FLAGS -o imslmp imslmp.f90 $LINK_F90
./imslmp

The expected output is as follows:


 Library version:  IMSL Fortran 90 MP Library Version 4.01
 Customer number:  999999
                               X
     1 -    5   9.320E-01  7.865E-01  5.004E-01  5.535E-01  9.672E-01

 *** TERMINAL ERROR 526 from s_error_post.  s_/rand_gen/ derived type option
 ***          array 'iopt' has undefined option (15) at entry (1).


LICENSE UPDATES: 

-- Replace the file /usr/local/vni2.1/license/license.dat with the current
license.dat file supplied by the vendor. 

%prep
%setup -q

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

cd $build_dir/files
find . -print | cpio -pdmuv $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
http://www.vni.com/products/imsl/

The file /usr/local/vni2.1/license/license.dat is a configuration file,
and is in the configuration server.  The Rutgers license number 
is 606926.  

The IMSL MATH/LIBRARY is a collection of FORTRAN routines and
functions useful in research and mathematical analysis. Each routine
is designed and documented to be used in research activities as well
as by technical specialists. To use any of these routines, you must
write a program in FORTRAN (or possibly some other language) to call
the MATH/LIBRARY routine. 

NB: You must have Fortran installed. 

See Installation_Notes in this directory for environment variables
recommended by the vendor.  

INSTALLATION: 

-- Install the rpm package. 

-- After the software has been copied to your system, connect to the
/usr/local/vni2.1 directory.  The next several steps are to validate
that it is working properly.  

-- Start a Bourne shell. 

.  ./CTT2.1/ctt/bin/cttsetup.sh

Note: This sets environment variables that are useful later

cd $CTT_EXAMPLES/f90/validate
$F90 $F90FLAGS -o imslmp imslmp.f90 $LINK_F90
./imslmp

The expected output is as follows:


 Library version:  IMSL Fortran 90 MP Library Version 4.01
 Customer number:  999999
                               X
     1 -    5   9.320E-01  7.865E-01  5.004E-01  5.535E-01  9.672E-01

 *** TERMINAL ERROR 526 from s_error_post.  s_/rand_gen/ derived type option
 ***          array 'iopt' has undefined option (15) at entry (1).


LICENSE UPDATES: 

-- Replace the file /usr/local/vni2.1/license/license.dat with the current
license.dat file supplied by the vendor. 
EOF

%files
%defattr(-,root,root)
/usr/local/vni%{version}
