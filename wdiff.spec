Summary: 	wdiff - Frontend to GNU diff
Name: 		wdiff
Version: 	0.5
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
%description
Compares two files on a word per word basis, finding the word deleted or added from the first file to make the 
second. A word is defined as anything between whitespace. It works by creating two temporary files, one word per 
line, and the executes 'diff' on these fields. It collects the 'diff' output and uses it to produce a nicer display 
of word differences between the original files. 

%prep
%setup -q

%build
./configure --prefix=/usr/local

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install prefix=%{buildroot}

%post
cat << EOF

%clean
rm -rf %{buildroot}

%files
%attr(0755, root, bin)  
/bin/wdiff
/info/wdiff.info
