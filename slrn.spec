Summary: Slang newsreader
Name: slrn
Version: 0.9.7.1
Release: 2
Group: Applications/Internet
Copyright: GPL
Source: slrn-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: slang inews
BuildRequires: slang-devel inews bash perl
Conflicts: vpkg-SFWslrn

%description
Slrn is a threaded newsreader for the console that uses the Slang
library.

%prep
%setup -q

%build
PATH="/usr/local/lib/news:$PATH" LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  ./configure 
# The Makefile checks for libslang during the make process; but it
# doesn't use -R.  Don't be fooled!  You don't need to edit your
# LD_LIBRARY_PATH when you actually -run- slrn.
LD_LIBRARY_PATH="/usr/local/lib" make

%install
perl -i -p -e 's(-e)(-r)' src/Makefile  # fix Linux idiom

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/doc
LD_LIBRARY_PATH="/usr/local/lib" make install prefix=$RPM_BUILD_ROOT/usr/local

mkdir -p $RPM_BUILD_ROOT/usr/local/doc/slrn-%{version}
cd $RPM_BUILD_ROOT/usr/local/share/doc/slrn
find . | cpio -pdm ../../../doc/slrn-%{version}
cd ..
rm -rf slrn

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To use slrn, set your NNTPSERVER environment variable to
news.rutgers.edu.
EOF

%files
%defattr(-,bin,bin)
/usr/local/doc/slrn-%{version}
/usr/local/share/slrn
/usr/local/man/man1/slrn.1
/usr/local/bin/slrn
