Summary: Tools to work with patchfiles
Name: patchutils
Version: 0.2.30
Release: 1
License: GPL
Group: Development/Tools
Source: %{name}-%{version}.tar.bz2
URL: http://cyberelk.net/tim/patchutils
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make

%description
Patchutils is a small collection of programs that operate on patch files.
-Interdiff generates an incremental patch from two patches against a common source.
-Combinediff generates a signel patch from two incremental patches, allowing you to merge patches together.
-Filterdiff will select the portions of a patch file that applt to files matching a shell wildcard.
-Fixcvsdiff is for correcting the output of 'cvs diff'.
-Rediff corrects hand-edited patches.
-Lsdiff displays a short listing of affected files in a patch file.
-Splitdiff separates out patches from a patch file so that each new patch files only alters any given file once.
-Grepdiff displays a list of the files modified by a patch where the patch contains a given regular expression.
-Recountdiff fices up counts and offset in a unified diff.
-Unwrapdiff fixes word-wrapped unified diffs.

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/ccs/bin:$PATH
CC="cc"
LD="ld"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC LD CPPFLAGS LDFLAGS

./configure
gmake

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/man/man1/*
