Summary: SAS statistical package
Name: sas
Version: 7
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
VENDOR WEB SITE: 

http://www.sas.com/

LICENSE UPDATES:  

The license that is part of this installation is set to expire 
on 30 June 2000. 

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., SAS v. 6.09, SAS v. 6.11 and SAS v. 6.12, SAS v. 7. 

On eden, these files are presently 

-- /usr/local/sas/sas609/setinit.sas (eden-backend only, and shared to
the front end machines)

--  /usr/local/sas611/setinit.sas 

--  /usr/local/sas612/setinit.sas 

-- /usr/local/sas7/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas for 609, 611, 612 and 7.

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sct01.  The file ./sashelp/core.sct01 is what is actually 
important to update.  

LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas7 to /usr/local/sas7/sas, i. e., 

ln -s /usr/local/sas7/sas /usr/local/bin/sas7

When (if) SAS 7 becomes the default version of SAS:  

	ln -s /usr/local/sas7/sas /usr/local/bin/sas 

The SASROOT for this version of SAS is /usr/local/sas7.  If you decide
to install SAS in a different directory, the SASROOT (top level
directory for SAS) must be changed.  This is accomplished by running
"sassetup" which is located the top level of the SAS package tree.
These functions are documented in: 

SASROOT/doc/install_instuctions.{htm,pdf,ps,txt}.

The file /usr/local/sas/sasv7.cfg points to the web site 
for online SAS docs.  They were not installed when this package was
generated.  

SPECIAL INSTRUCTIONS FOR TINT PACKAGE: 

mkdir -p  /sos/licensed/sas/
mount -r  alfred:/sos/licensed/sas/ /sos/licensed/sas/ 

/sos/dist/tarballs/installpackage beta sas7 

B. Binde 
August 10, 1999 

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

http://www.sas.com/

LICENSE UPDATES:  

The license that is part of this installation is set to expire 
on 30 June 2000. 

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., SAS v. 6.09, SAS v. 6.11 and SAS v. 6.12, SAS v. 7. 

On eden, these files are presently 

-- /usr/local/sas/sas609/setinit.sas (eden-backend only, and shared to
the front end machines)

--  /usr/local/sas611/setinit.sas 

--  /usr/local/sas612/setinit.sas 

-- /usr/local/sas7/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas for 609, 611, 612 and 7.

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sct01.  The file ./sashelp/core.sct01 is what is actually 
important to update.  

LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas7 to /usr/local/sas7/sas, i. e., 

ln -s /usr/local/sas7/sas /usr/local/bin/sas7

When (if) SAS 7 becomes the default version of SAS:  

	ln -s /usr/local/sas7/sas /usr/local/bin/sas 

The SASROOT for this version of SAS is /usr/local/sas7.  If you decide
to install SAS in a different directory, the SASROOT (top level
directory for SAS) must be changed.  This is accomplished by running
"sassetup" which is located the top level of the SAS package tree.
These functions are documented in: 

SASROOT/doc/install_instuctions.{htm,pdf,ps,txt}.

The file /usr/local/sas/sasv7.cfg points to the web site 
for online SAS docs.  They were not installed when this package was
generated.  

SPECIAL INSTRUCTIONS FOR TINT PACKAGE: 

mkdir -p  /sos/licensed/sas/
mount -r  alfred:/sos/licensed/sas/ /sos/licensed/sas/ 

/sos/dist/tarballs/installpackage beta sas7 

B. Binde 
August 10, 1999 
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/sas7
