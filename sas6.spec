Summary: SAS statistical package
Name: sas
Version: 6.1.2
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
Vendor web site:  http://www.sas.com/


LICENSE RENEWAL:  

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., v. 6.12.

On eden, these files are presently (on an NFS server and shared to
the front end machines): 

--  /usr/local/sas612/setinit.sas 

--  /usr/local/sas612a/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas. 

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sct01.  The file ./sashelp/core.sct01 is what is actually 
important to update.  It has been updated in this sas612 package 
to expire on 30 June 2000 

RECOMMENDED LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas612 to /usr/local/sas612/sas.  For example:  

ln -s /usr/local/sas612a/sas /usr/local/bin/sas612

When (if) SAS 612 becomes the default version of SAS:  

	ln -s /usr/local/sas612/sas /usr/local/bin/sas 

CHANGING THE SASROOT: 

The SASROOT is the path to the directory containing the SAS 
executable.  It is hardcoded in the sas binary.  

The SASROOT for this version of SAS is /local/sas612a.  In order to get
the executable to run, 

mkdir -p /local
chmod 755 /local 
ln -s /usr/local/sas612a /local/sas612a

To change the SASROOT, install the package. 

	-- make sure the directory has the name that you want it to be 

	-- cd to new directory (example: /local/sas612a)

	-- run this command:  

./utilities/bin/patchname <sas binary> <new dir name>

Example:

./utilities/bin/patchname ./sas /local/sas612a





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
Vendor web site:  http://www.sas.com/


LICENSE RENEWAL:  

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., v. 6.12.

On eden, these files are presently (on an NFS server and shared to
the front end machines): 

--  /usr/local/sas612/setinit.sas 

--  /usr/local/sas612a/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas. 

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sct01.  The file ./sashelp/core.sct01 is what is actually 
important to update.  It has been updated in this sas612 package 
to expire on 30 June 2000 

RECOMMENDED LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas612 to /usr/local/sas612/sas.  For example:  

ln -s /usr/local/sas612a/sas /usr/local/bin/sas612

When (if) SAS 612 becomes the default version of SAS:  

	ln -s /usr/local/sas612/sas /usr/local/bin/sas 

CHANGING THE SASROOT: 

The SASROOT is the path to the directory containing the SAS 
executable.  It is hardcoded in the sas binary.  

The SASROOT for this version of SAS is /local/sas612a.  In order to get
the executable to run, 

mkdir -p /local
chmod 755 /local 
ln -s /usr/local/sas612a /local/sas612a

To change the SASROOT, install the package. 

	-- make sure the directory has the name that you want it to be 

	-- cd to new directory (example: /local/sas612a)

	-- run this command:  

./utilities/bin/patchname <sas binary> <new dir name>

Example:

./utilities/bin/patchname ./sas /local/sas612a
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/sas612a
