Summary: IMSL math library
Name: imsl
Version: 1.0
Release: 3
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar
AutoReqProv: no

%description
http://www.vni.com/products/imsl/

The file /usr/local/vni/license/license.dat is a configuration file,
and is in the configuration server.  The Rutgers site id number is
603631.

The IMSL MATH/LIBRARY is a collection of FORTRAN routines and
functions useful in research and mathematical analysis. Each routine
is designed and documented to be used in research activities as well
as by technical specialists. To use any of these routines, you must
write a program in FORTRAN (or possibly some other language) to call
the MATH/LIBRARY routine. 

NB: You must have Fortran installed. 

INSTALLATION: 

-- Be sure that you have the Rutgers University license number as well
as softkeys from the vendor. These are available by contacting the New
Brunswick Computing Services, Eva Michna
<michna@nbcs.rutgers.edu>. 

-- Install the package. 

-- After the software has been copied to your system, connect to the
/usr/local/vni directory. 

		If running csh: 

		source ipt/bin/iptsetup.csh

		If running Korn, Bourne or Bash 

		. ipt/bin/iptsetup.sh 

-- Continue by typing the following: 

cd $LICENSE_DIR 

VNI_ENTER_SOFTKEY

and enter the softkey provided by the vendor. 

Type quit when you have typed in all of the softkeys from the vendor.

--  You will then be asked to enter the VNI License Number. 

--  To test the install, 

cd /usr/local/vni/examples/fnl 
$FC -o fnl $FFLAGS fnl.f $LINK_FNL 

-- Execute the program. 

./fnl 

-- The expected output from the test is:

                                  X
                               1  2  3
                         1.000  1.500  1.000

LICENSE UPDATES: 

-- Replace the file /usr/local/vni/license/license.dat with the current
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

The file /usr/local/vni/license/license.dat is a configuration file,
and is in the configuration server.  The Rutgers site id number is
603631.

The IMSL MATH/LIBRARY is a collection of FORTRAN routines and
functions useful in research and mathematical analysis. Each routine
is designed and documented to be used in research activities as well
as by technical specialists. To use any of these routines, you must
write a program in FORTRAN (or possibly some other language) to call
the MATH/LIBRARY routine. 

NB: You must have Fortran installed. 

INSTALLATION: 

-- Be sure that you have the Rutgers University license number as well
as softkeys from the vendor. These are available by contacting the New
Brunswick Computing Services, Eva Michna
<michna@nbcs.rutgers.edu>. 

-- Install the package. 

-- After the software has been copied to your system, connect to the
/usr/local/vni directory. 

		If running csh: 

		source ipt/bin/iptsetup.csh

		If running Korn, Bourne or Bash 

		. ipt/bin/iptsetup.sh 

-- Continue by typing the following: 

cd $LICENSE_DIR 

VNI_ENTER_SOFTKEY

and enter the softkey provided by the vendor. 

Type quit when you have typed in all of the softkeys from the vendor.

--  You will then be asked to enter the VNI License Number. 

--  To test the install, 

cd /usr/local/vni/examples/fnl 
$FC -o fnl $FFLAGS fnl.f $LINK_FNL 

-- Execute the program. 

./fnl 

-- The expected output from the test is:

                                  X
                               1  2  3
                         1.000  1.500  1.000

LICENSE UPDATES: 

-- Replace the file /usr/local/vni/license/license.dat with the current
license.dat file supplied by the vendor. 

EOF

%files
%defattr(-,root,root)
/usr/local/man/man1/*
/usr/local/vni
/usr/local/doc/vni
