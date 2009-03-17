%include machine-header.spec

Name: 		binutils
Version: 	2.19.1
Release:	1	
License: 	GPL
Group: 		Development/Tools
Source: 	ftp://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.gz
URL:		http://www.gnu.org/software/binutils/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: 	python, texinfo
Summary: 	GNU binutils

%description
The GNU Binutils are a collection of binary tools. The main ones are:

    * ld - the GNU linker.
    * as - the GNU assembler.

But they also include:

    * addr2line - Converts addresses into filenames and line numbers.
    * ar - A utility for creating, modifying and extracting from archives.
    * c++filt - Filter to demangle encoded C++ symbols.
    * dlltool - Creates files for building and using DLLs.
    * gold - A new, faster, ELF only linker, still in beta test.
    * gprof - Displays profiling information.
    * nlmconv - Converts object code into an NLM.
    * nm - Lists symbols from object files.
    * objcopy - Copys and translates object files.
    * objdump - Displays information from object files.
    * ranlib - Generates an index to the contents of an archive.
    * readelf - Displays information from any ELF format object file.
    * size - Lists the section sizes of an object or archive file.
    * strings - Lists printable strings from files.
    * strip - Discards symbols.
    * windmc - A Windows compatible message compiler.
    * windres - A compiler for Windows resource files.

Most of these programs use BFD, the Binary File Descriptor library, to do 
low-level manipulation. Many of them also use the opcodes library to assemble 
and disassemble machine instructions.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure 				\
	--prefix=%{_prefix}/gnu		\
	--mandir=%{_prefix}/gnu/man	\
	--infodir=%{_prefix}/gnu/info	\
	--disable-nls
gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
%{_bindir}/unhardlinkify.py %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/as.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/binutils.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/bfd.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/configure.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/gprof.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/ld.info
	%{_bindir}/install-info --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/standards.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/as.info
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/bfd.info
	%{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
		%{_prefix}/gnu/info/binutils.info
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/configure.info
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/gprof.info
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/ld.info
        %{_bindir}/install-info --delete --info-dir=%{_prefix}/gnu/info \
                %{_prefix}/gnu/info/standards.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog
%{_prefix}/gnu/bin/*
%{_prefix}/gnu/%{sparc_arch}/bin/*
%{_prefix}/gnu/%{sparc_arch}/lib/ldscripts/*
%{_prefix}/gnu/info/*
%{_prefix}/gnu/include/*
%{_prefix}/gnu/lib/*
%{_prefix}/gnu/man/man*/*

%changelog
* Tue Mar 17 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.19.1-1
- Updated to version 2.19.1
- Removed patch (no longer needed)
- GNU strip is now packaged (the bug has apparently been fixed)
* Tue Jun 24 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> 2.18-2
- Disabled NLS
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 2.18-1
- Added binutils-suncc.patch, updated to version 2.18
* Mon Aug 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> 2.17-1
- Cleaned up spec file, updated to 2.17
