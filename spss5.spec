Summary: SPSS statistical package version 5.0
Name: spss
Version: 5.0
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar
Provides: spssmagg.so
Provides: spssmano.so
Provides: spssmbrk.so
Provides: spssmcde.so
Provides: spssmcrs.so
Provides: spssmeda.so
Provides: spssmfre.so
Provides: spssmmre.so
Provides: spssmnew.so
Provides: spssmnpt.so
Provides: spssmone.so
Provides: spssmpar.so
Provides: spssmpea.so
Provides: spssmspr.so
Provides: spssmtte.so
Provides: spssmuse.so
Provides: libhoops.so
Provides: spsscifi.so
Provides: spsscigi.so
Provides: spsscori.so
Provides: spsscsyi.so
Provides: spssmals.so
Provides: spssmclu.so
Provides: spssmdsc.so
Provides: spssmfac.so
Provides: spssmkme.so
Provides: spssmprx.so
Provides: spssmrel.so
Provides: spssmcox.so
Provides: spssmhil.so
Provides: spssmkm.so
Provides: spssmlgr.so
Provides: spssmlog.so
Provides: spssmman.so
Provides: spssmmtc.so
Provides: spssmnlr.so
Provides: spssmpro.so
Provides: spssmsur.so
Provides: spssmtbu.so
Provides: spssm2sl.so
Provides: spssmacf.so
Provides: spssmari.so
Provides: spssmexs.so
Provides: spssmext.so
Provides: spssmfit.so
Provides: spssmsea.so
Provides: spssmspc.so
Provides: spssmtsp.so
Provides: spssmtsu.so
Provides: spssmver.so
Provides: spssmwls.so
Provides: spssmx11.so
Provides: spssmldn.so
Provides: spssmmar.so

%description
http://www.spss.com/

The file /usr/local/bin/spss.example is provided as an example file
for invoking SPSS.  It will need to be changed according the the 
actual location of the package and any site specific characteristics.  

Because the package is large, many sysadmins will most likely want
to install the package on a partition that can later be shared.  

Licensing of the package is controlled by the lisense.dat file, found
under the SPSS/licenses directory.  A version of this file is
provided.  However, it is possible the license file in the package
might be outdated.  The current contact person for SPSS license file
updates is Pat Douglas (douglas@nbcs). 

When remapping SPSS, keep the following in mind: 

From:  http://www.spss.com/tech/unixfaq.html

If SPSS has been installed in a non-default directory, some editing
needs to be done to the shell script called "spss". It is located in
the bin subdirectory of the installation directory. You can edit it
with the vi editor (assuming you have appropriate privileges for the
file) and you'll need to change the environment variable SPSS_ROOT to
indicate the directory SPSS was installed into. 

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
http://www.spss.com/

The file /usr/local/bin/spss.example is provided as an example file
for invoking SPSS.  It will need to be changed according the the 
actual location of the package and any site specific characteristics.  

Because the package is large, many sysadmins will most likely want
to install the package on a partition that can later be shared.  

Licensing of the package is controlled by the lisense.dat file, found
under the SPSS/licenses directory.  A version of this file is
provided.  However, it is possible the license file in the package
might be outdated.  The current contact person for SPSS license file
updates is Pat Douglas (douglas@nbcs). 

When remapping SPSS, keep the following in mind: 

From:  http://www.spss.com/tech/unixfaq.html

If SPSS has been installed in a non-default directory, some editing
needs to be done to the shell script called "spss". It is located in
the bin subdirectory of the installation directory. You can edit it
with the vi editor (assuming you have appropriate privileges for the
file) and you'll need to change the environment variable SPSS_ROOT to
indicate the directory SPSS was installed into. 
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/SPSS
/usr/local/bin/*
