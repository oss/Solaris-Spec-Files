%define sl_ver 1.4.4
%define doc_ver 1.4.3

Summary: Slang language
Name: slang
Version: %{sl_ver}
Release: 2
Group: Development/Languages
Copyright: GPL/Artistic
Source0: slang-%{sl_ver}.tar.bz2
Source1: slang%{doc_ver}-doc.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWslang

%description
S-Lang is an interpreted language that was designed from the start to
be easily embedded into a program to provide it with a powerful
extension language.  Examples of programs that use S-Lang as an
extension language include the jed text editor, the slrn newsreader,
and sldxe (unreleased), a numerical computation program.  For this
reason, S-Lang does not exist as a separate application. 

    [ from the manual ]

%package devel
Summary: Slang headers and static libraries
Group: Development/Libraries
Requires: slang = %{version}

%description devel
Slang-devel contains the headers and static libraries for slang; you
need this package if you are building software with slang.

%package doc
Summary: Slang documentation
Group: Documentation

%description doc
Slang-doc contains auxiliary slang documentation, available on the
Internet at ftp://space.mit.edu/pub/davis/slang/.

%prep
%setup -q
%setup -q -D -T -a 1

%build
./configure
make elf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc/slang-%{version}
make install prefix=$RPM_BUILD_ROOT/usr/local
make install-elf prefix=$RPM_BUILD_ROOT/usr/local
make install-links prefix=$RPM_BUILD_ROOT/usr/local
cd doc
find . | cpio -pdmu $RPM_BUILD_ROOT/usr/local/doc/slang-%{version}
cd $RPM_BUILD_ROOT/usr/local/doc
mv slang/* slang-%{version}
rmdir slang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/lib/libslang.a
/usr/local/include/*


%files doc
%defattr(-,bin,bin)
/usr/local/doc/slang-%{version}
