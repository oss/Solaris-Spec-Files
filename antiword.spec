Summary:	Antiword - Free MS Word Reader
Name:	 	antiword	
Version:	0.37
Release:	2
Copyright:	GPL
Group:		Applications/Productivity
URL:		http://www.winfield.demon.nl/
Vendor:		NBCS/OSS
Packager:       Jonathan Kaczynski <jmkacz@oss.rutgers.edu>
Source: 	%{name}-%{version}.tar.gz
Patch:          %{name}-%{version}.patch
BuildRoot:	%{_tmppath}/%{name}-root

%description
Antiword  is  an  application  that displays the text and the images of
Microsoft Word documents.
A wordfile named - stands for a Word document read  from  the  standard
input.
Only  documents  made  by  MS Word version 2 and version 6 or later are
supported.


%prep
%setup -q
%patch -p1
# How do I make diff not follow softlinks? (To make the patch I rm'ed the
# softlink `Makefile` from both directories)
# Change the buildroot in the Makefile depending on what it is in the spec file
sed "s|BR|%{buildroot}|" Makefile > Makefile.2
mv Makefile.2 Makefile

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/share/antiword
mkdir -p %{buildroot}/usr/local/man/man1
cp Docs/antiword.1 %{buildroot}/usr/local/man/man1
make global_install
rm %{buildroot}/usr/local/bin/kantiword

%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root)
%doc Docs/*
%attr(0755, root, root)/usr/local/bin/antiword
/usr/local/share/antiword/*
/usr/local/man/man1/antiword.1

%changelog
* Tue Feb 07 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.37-1
 - Updated to latest version
* Mon May 19 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Oops. Fun with attributes.
* Fri Jan  3 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed to make it actually work, edited antiword.h to allow for /usr/local/share
* Mon Dec 23 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - initial rutgers rpm ho ho ho

