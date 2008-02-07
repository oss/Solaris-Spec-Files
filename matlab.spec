
Summary: matrix based math program for scientists and engineers
Name: matlab
Version: 7.4.0
Release: 2
Group: Applications/Scientific
Copyright: Licensed
Packager: David Diffenbaugh
Source: %{name}-%{version}.tar.gz
#Install matlab using the DVD into /usr/local/matlab74
#then mkdir /usr/local/matlab-7.4.0 and cp -r matlab74 /usr/local/matlab-7.4.0
#do tar cf matlab-7.4.0.tar matlab-7.4.0
#Make sure the BuildRoot you specifiy is large enough to handle the files
#Matlab is about 2.3 GB
BuildRoot: /tmp/%{name}-root
AutoReq: 0
AutoProv: 0
#The above turn off the find-provides and find-requires dependency handler


%description
MATLAB is a high-level language and interactive environment that enables
you to perform computationally intensive tasks faster than with traditional
programming languages such as C, C++, and Fortran. 


%prep
%setup -q

%build
mkdir %{buildroot}

%install
cd %{buildroot} 
mkdir -p usr/local
cd usr/local
cp -r  /usr/local/src/rpm-packages/BUILD/matlab-7.4.0/matlab74 .
ln -s matlab74 matlab

%post
cat <<EOF
http://www.mathworks.com

INSTALLATION:
 
o The installation is located in /usr/local/matlab

LICENSE SETUP:

o Matlab requires a valid license. For an example license file check out:
    /usr/local/matlab/etc/license.dat.example

o Rutgers Faculty,Staff and Students can download a license file from:
    http://software.rutgers.edu on the Mathematical Applications page

o Copy the license to the /usr/local/matlab/etc directory

o Rename the license file and set the permissions to 644
    mv Mathworks_2007b_Linux_MAC_Sun_License_File.txt license.dat
    chmod 644 license.dat 
    
EXECUTION:

o Invoke the program with the command: /usr/local/matlab/bin/matlab
    
o You may wish to create the following symlinks in /usr/local/bin:
    ln -s /usr/local/matlab/bin/matlab /usr/local/bin/matlab
    ln -s /usr/local/matlab/bin/mbuild /usr/local/bin/mbuild
    ln -s /usr/local/matlab/bin/mex /usr/local/bin/mex
    ln -s /usr/local/matlab/bin/mcc /usr/local/bin/mcc-matlab

NOTE: We have linked mcc to mcc-matlab because mcc may conflict with other
      licensed software packages (i.e. Mathematica). If you do not have mcc
      conflicts you can remove the '-matlab' suffix from the mcc link. You 
      may want /usr/local/bin/mcc to be a script that informs the user of
      the new mcc naming scheme (i.e. mcc-matlab, mcc-mathematica). 

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/*


%changelog
* Tue Feb 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 7.4.0-2
- installed into matlab74 instead  matlab-7.4.0/matlab74
* Thu Jan 30 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 7.4.0-1
- updated to 7.4.0 
