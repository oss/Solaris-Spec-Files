Summary: SAS statistical package
Name: sas
Version: 8.1
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
Vendor web site:  http://www.sas.com/

Local documentation web site:  http://www.sas.reference.rutgers.edu

LICENSE RENEWAL:  

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., v. 8.1.

On eden, these files are presently (on an NFS server and shared to
the front end machines): 

--  /nirvana/export/sas81/setinit.sas 

--  /nirvana/export/sas81/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas. 

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sas7bcat.  The file ./sashelp/core.sas7bcat is what is actually 
important to update.  It has been updated in this sas81 package 
to expire on 30 June 2001.  

RECOMMENDED LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas81 to /usr/local/sas81/sas.  For example:  

ln -s /usr/local/sas81/sas /usr/local/bin/sas81

When (if) SAS 8.1 becomes the default version of SAS:  

	ln -s /usr/local/sas81/sas /usr/local/bin/sas 

CHANGING THE SASROOT: 

The SASROOT is the path to the directory containing the SAS 
executable.  It is hardcoded in the sas binary.  

The SASROOT for this version of SAS is 

/usr/local/sas81

The SASROOT must correspond to the actual directory name 
where the files are located.  

To change the SASROOT, install the package. 

	-- make sure the directory has the name that you want it to be 

	-- cd to new directory (example: /local/sas81)

	-- run this command:  

./utilities/bin/patchname <sas binary> <new dir name>

Example:

./utilities/bin/patchname ./sas /local/sas81

If the files are actually in /nirvana/export/sas81, the SASROOT must
be patched as above.  Make sure that /nirvana/export (or whatever the
partition may be called) is shared properly. Then on the front end
machines:

ln -s /nirvana/export/sas81/sas /usr/local/bin/sas81

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

Local documentation web site:  http://www.sas.reference.rutgers.edu

LICENSE RENEWAL:  

When sas is nearing license expiration, it will issue warning messages. 

Obtain the new license files from the vendor and place in setinit.sas
for each version, e. g., v. 8.1.

On eden, these files are presently (on an NFS server and shared to
the front end machines): 

--  /nirvana/export/sas81/setinit.sas 

--  /nirvana/export/sas81/setinit.sas 


On rci, cd /rci/local/sas* and edit setinit.sas. 

After enabling privilages, connect to the directory containing the 
updated setinit.sas

./sas -setinit setinit.sas

This will create a new setinit.log in that directory and also change 
./sashelp/core.sas7bcat.  The file ./sashelp/core.sas7bcat is what is actually 
important to update.  It has been updated in this sas81 package 
to expire on 30 June 2001.  

RECOMMENDED LINKS: 

To make it easier for users to run an appropriate version of SAS, 
link /usr/local/bin/sas81 to /usr/local/sas81/sas.  For example:  

ln -s /usr/local/sas81/sas /usr/local/bin/sas81

When (if) SAS 8.1 becomes the default version of SAS:  

	ln -s /usr/local/sas81/sas /usr/local/bin/sas 

CHANGING THE SASROOT: 

The SASROOT is the path to the directory containing the SAS 
executable.  It is hardcoded in the sas binary.  

The SASROOT for this version of SAS is 

/usr/local/sas81

The SASROOT must correspond to the actual directory name 
where the files are located.  

To change the SASROOT, install the package. 

	-- make sure the directory has the name that you want it to be 

	-- cd to new directory (example: /local/sas81)

	-- run this command:  

./utilities/bin/patchname <sas binary> <new dir name>

Example:

./utilities/bin/patchname ./sas /local/sas81

If the files are actually in /nirvana/export/sas81, the SASROOT must
be patched as above.  Make sure that /nirvana/export (or whatever the
partition may be called) is shared properly. Then on the front end
machines:

ln -s /nirvana/export/sas81/sas /usr/local/bin/sas81
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/sas81
