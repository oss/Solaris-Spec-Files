Summary: SPSS statistical package version 6.1.3
Name: spss
Version: 6.1.3
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar
Provides: spssadv.so
Provides: spsscat.so
Provides: spsscapi.so
Provides: libhoops.so
Provides: spsstrnd.so
Provides: spsstrnp.so
Provides: spssaddc.so
Provides: spsstabl.so
Provides: spssde.so
Provides: spssedit.so
Provides: spssheap.so
Provides: spssm2sl.so
Provides: spssmacf.so
Provides: spssmagg.so
Provides: spssmals.so
Provides: spssmano.so
Provides: spssmari.so
Provides: spssmbrk.so
Provides: spssmcde.so
Provides: spssgraf.so
Provides: spssmclu.so
Provides: spssmcox.so
Provides: spssmcrs.so
Provides: spssmdev.so
Provides: spssmdsc.so
Provides: spssmeda.so
Provides: spssmexs.so
Provides: spssmext.so
Provides: spssmfac.so
Provides: spssmfit.so
Provides: spssmfre.so
Provides: spssmgen.so
Provides: spssmhil.so
Provides: spssmkm.so
Provides: spssmkme.so
Provides: spssmldn.so
Provides: spssmlgr.so
Provides: spssmlog.so
Provides: spssmman.so
Provides: spssmmar.so
Provides: spssmmre.so
Provides: spssmmtc.so
Provides: spssmnew.so
Provides: spssmnlr.so
Provides: spssmnpt.so
Provides: spssmone.so
Provides: spssmpar.so
Provides: spssmpea.so
Provides: spssmpro.so
Provides: spssmprx.so
Provides: spssmrel.so
Provides: spssmsea.so
Provides: spssmspc.so
Provides: spssmspr.so
Provides: spssmsur.so
Provides: spssmtbu.so
Provides: spssmtsu.so
Provides: spssmtte.so
Provides: spssmuse.so
Provides: spssmver.so
Provides: spssmwls.so
Provides: spssmx11.so
Provides: spssprnt.so
Provides: spadsave.so

%description
VENDOR WEB SITE:  
 
http://www.spss.com/ 

includes usage notes and technical FAQs 

INSTALLTION NOTES: 

After installing the package,  
 
-- Make the X11 resources file available:   
 
ln -s /usr/local/SPSS613/bin/SPSS.defaults /usr/openwin/lib/app-defaults/SPSS  

-- Link to needed libraries: 

ln -s /usr/dt/lib/libMrm.so.3  /usr/openwin/lib/libMrm.so        
ln -s /usr/dt/lib/libUil.so.3     /usr/openwin/lib/libUil.so
ln -s /usr/dt/lib/libXm.so.3    /usr/openwin/lib/libXm.so
ln -s /usr/dt/lib/libMrm.so.3  /usr/openwin/lib/libMrm.so.2
ln -s /usr/dt/lib/libXm.so.3    /usr/openwin/lib/libXm.so.2
 
--- Set up softlink to the spss shell script, i. e.,  
 
ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss613  
 
	When this version of SPSS becomes the default on the system,  
 
ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss  
 
LICENSING:  

Licensing of the package is controlled by the lisense.dat file, found
under the SPSS/licenses directory.  A version of this file is provided
in the package.  However, the license file in the package might be
outdated.  system. The current contact person for SPSS license file
updates is Pat Douglas (douglas@nbcs.rutgers.edu).  The file is 
also on the NBCS config system.  

OTHER NOTES:  

When remapping SPSS, keep the following in mind: 

Quoted from: http://www.spss.com/tech/unixfaq.html

If SPSS has been installed in a non-default directory, some editing
needs to be done to the shell script called "spss". It is located in
the bin subdirectory of the installation directory. You can edit it
with the vi editor (assuming you have appropriate privileges for the
file) and you'll need to change the environment variable SPSS_ROOT to
indicate the directory SPSS was installed into. 

===========

Notes on building the package (for package maintainer): 


--  Extract files from installation tape into $HOME/spss613

        -- Insert the 4mm tape into the tape drive 
        -- cd /tmp 
        -- mkdir spss 
        -- tar -xvf /dev/rmt/1  (substitute appropriate device name) 
        -- cd /tmp/spss
        -- uncompress spssinst.Z 

--  mkdir -p /tmp/install/

--  cp -p $HOME/spss613/install/spssinst /tmp/install/spssinst

--  Re-create tar ball as spss613.tar

--   Run the spssinst install script.  When asked for media, 
supply $HOME/spss613.tar as the location. 

SPSS Software Site ID: 201209

--  Update license.dat file with appropriate version.  File should 
be a DEMO license with an expiration date some time in the future. 

-- Make the X11 resources file available:  

ln -s /usr/local/SPSS613/bin/SPSS.defaults /usr/openwin/lib/app-defaults/SPSS 

-- Modify the value SPSS_ROOT in /usr/local/SPSS613/bin/spss.  The 
installation procedure sets it to the "default" location of:  

SPSS_ROOT=/usr/lpp/SPSS;  export SPSS_ROOT

The script has been modified to: 

SPSS_ROOT=/usr/local/SPSS613;  export SPSS_ROOT

--- Set up softlink to the SPSS shell script, i. e., 

ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss613 

When this version of SPSS becomes the default on the system, 

ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss 

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
VENDOR WEB SITE:  
 
http://www.spss.com/ 

includes usage notes and technical FAQs 

INSTALLTION NOTES: 

After installing the package,  
 
-- Make the X11 resources file available:   
 
ln -s /usr/local/SPSS613/bin/SPSS.defaults /usr/openwin/lib/app-defaults/SPSS  

-- Link to needed libraries: 

ln -s /usr/dt/lib/libMrm.so.3  /usr/openwin/lib/libMrm.so        
ln -s /usr/dt/lib/libUil.so.3     /usr/openwin/lib/libUil.so
ln -s /usr/dt/lib/libXm.so.3    /usr/openwin/lib/libXm.so
ln -s /usr/dt/lib/libMrm.so.3  /usr/openwin/lib/libMrm.so.2
ln -s /usr/dt/lib/libXm.so.3    /usr/openwin/lib/libXm.so.2
 
--- Set up softlink to the spss shell script, i. e.,  
 
ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss613  
 
	When this version of SPSS becomes the default on the system,  
 
ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss  
 
LICENSING:  

Licensing of the package is controlled by the lisense.dat file, found
under the SPSS/licenses directory.  A version of this file is provided
in the package.  However, the license file in the package might be
outdated.  system. The current contact person for SPSS license file
updates is Pat Douglas (douglas@nbcs.rutgers.edu).  The file is 
also on the NBCS config system.  

OTHER NOTES:  

When remapping SPSS, keep the following in mind: 

Quoted from: http://www.spss.com/tech/unixfaq.html

If SPSS has been installed in a non-default directory, some editing
needs to be done to the shell script called "spss". It is located in
the bin subdirectory of the installation directory. You can edit it
with the vi editor (assuming you have appropriate privileges for the
file) and you'll need to change the environment variable SPSS_ROOT to
indicate the directory SPSS was installed into. 

===========

Notes on building the package (for package maintainer): 


--  Extract files from installation tape into $HOME/spss613

        -- Insert the 4mm tape into the tape drive 
        -- cd /tmp 
        -- mkdir spss 
        -- tar -xvf /dev/rmt/1  (substitute appropriate device name) 
        -- cd /tmp/spss
        -- uncompress spssinst.Z 

--  mkdir -p /tmp/install/

--  cp -p $HOME/spss613/install/spssinst /tmp/install/spssinst

--  Re-create tar ball as spss613.tar

--   Run the spssinst install script.  When asked for media, 
supply $HOME/spss613.tar as the location. 

SPSS Software Site ID: 201209

--  Update license.dat file with appropriate version.  File should 
be a DEMO license with an expiration date some time in the future. 

-- Make the X11 resources file available:  

ln -s /usr/local/SPSS613/bin/SPSS.defaults /usr/openwin/lib/app-defaults/SPSS 

-- Modify the value SPSS_ROOT in /usr/local/SPSS613/bin/spss.  The 
installation procedure sets it to the "default" location of:  

SPSS_ROOT=/usr/lpp/SPSS;  export SPSS_ROOT

The script has been modified to: 

SPSS_ROOT=/usr/local/SPSS613;  export SPSS_ROOT

--- Set up softlink to the SPSS shell script, i. e., 

ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss613 

When this version of SPSS becomes the default on the system, 

ln -s /usr/local/SPSS613/bin/spss /usr/local/bin/spss 
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/SPSS613
