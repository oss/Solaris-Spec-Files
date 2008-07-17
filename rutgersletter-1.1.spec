%define mtex usr/local/teTeX/share/texmf
%define mloc usr/local/teTeX/share/texmf-local

Summary:	Rutgers Letterhead
Name:		rutgersletter
Version:	1.1
Release:	2
License:	Rutgers OSS
Group:		none
Source:		rutgersletter-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Distribution:	Rutgers OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Requires:	teTeX
BuildRequires:	teTeX

%description
teTex add-on for letter headers, footers, and formatting.

%prep
%setup -q

%build
#nothing to build

%install
rm -rf %{buildroot}

TEMPMF="usr/local/teTeX/share/texmf"
TEMPLOCAL="usr/local/teTeX/share/texmf-local"
export TEMPLOCAL TEMPMF

mkdir -p %{buildroot}/$TEMPLOCAL
mkdir -p %{buildroot}/$TEMPMF

cp -rpf $RPM_BUILD_DIR/rutgersletter-%{version}/local/* %{buildroot}/$TEMPLOCAL
cp -rpf $RPM_BUILD_DIR/rutgersletter-%{version}/texmf/* %{buildroot}/$TEMPMF

%preun
	#Solaris
	TEMPMF="usr/local/teTeX/share/texmf"
	
	#check teTeX, updmap, and texhash
	if [ -d /usr/local/teTeX ]; then

		TTEKDIR="usr/local/teTeX"
		
		for upds in `find /$TTEKDIR -name 'updmap-sys'`;
		do
			if [ -n `file $upds | sed '/executable/!d;'` ]; then
				UPDLOC=$upds
				break
			fi
		done
		
		if [ -z "$UPDLOC" ]; then
			for upds in `find /$TTEKDIR -name 'updmap'`;
			do
				if [ -n "`file $upds | sed '/executable/!d;'`" ]; then
					UPDLOC=$upds
					break
				fi
			done
		fi
		
		if [ -z "$UPDLOC" ]; then
			echo "You have a teTeX directory, but I cannot find updmap. Exiting..."
			exit 1
		fi

		for thashes in `find /$TTEKDIR -name 'texhash'`;
		do
			if [ -n "`file $thashes | sed '/executable/!d;'`" ]; then
				TEXHASHLOC=$thashes
				break
			fi
		done
		
		if [ -z "$TEXHASHLOC" ]; then
			echo "You have a teTeX directory, but I cannot find texhash. Exiting..."
			exit 1
		fi
		
		#cut off last part
		TEXHASHLOC=`echo $TEXHASHLOC | sed s:/texhash::g`
		UPDLOC=`echo $UPDLOC | sed s:/updmap-sys::g | sed s:/updmap::g`
		
		#fix path
		PATH=$UPDLOC:$TEXHASHLOC:$PATH
	else
		echo "You do not have teTeX at /usr/local/teTeX . Exiting..."
		exit 1
	fi
	
	if [ -n "`uname -a | sed '/5\.8/!d;'`" ]; then
		#Solaris 8
		TEMPLOCAL="usr/local/teTeX/share/texmf.local"
		TEMPOS="solaris8"
	elif [ -n "`uname -a | sed '/5\.9/!d;'`" ]; then
		#Solaris 9
		TEMPLOCAL="usr/local/teTeX/share/texmf-local"
		TEMPOS="solaris9"
	else
		echo "This package is only for Solaris 8 and 9."
		exit 1
	fi

export TEMPLOCAL;
export TEMPMF;
export TEMPOS;
export PATH;
export TTEKDIR;
export UPDLOC;
export TEXHASHLOC;

#run texhash
	#echo "Solaris 9"
	if [ -f $TEXHASHLOC/texhash ]; then
		$TEXHASHLOC/texhash
	fi

#finish up
	#echo "Solaris 9"
	if [ -f $UPDLOC/updmap-sys ]; then
		$UPDLOC/updmap-sys --disable bera.map --quiet >/dev/null 2>/dev/null
		sleep 3
		$UPDLOC/updmap-sys --quiet >/dev/null 2>/dev/null
	elif [ -f $UPDLOC/updmap ]; then
		$UPDLOC/updmap --disable bera.map --quiet >/dev/null 2>/dev/null
		sleep 3
		$UPDLOC/updmap --quiet >/dev/null 2>/dev/null
	fi
exit 0

%post
#check os
	#Solaris
	TEMPMF="usr/local/teTeX/share/texmf"
	
	#check teTeX, updmap, and texhash
	if [ -d /usr/local/teTeX ]; then

		TTEKDIR="usr/local/teTeX"
		
		for upds in `find /$TTEKDIR -name 'updmap-sys'`;
		do
			if [ -n `file $upds | sed '/executable/!d;'` ]; then
				UPDLOC=$upds
				break
			fi
		done
		
		if [ -z "$UPDLOC" ]; then
			for upds in `find /$TTEKDIR -name 'updmap'`;
			do
				if [ -n "`file $upds | sed '/executable/!d;'`" ]; then
					UPDLOC=$upds
					break
				fi
			done
		fi
		
		if [ -z "$UPDLOC" ]; then
			echo "You have a teTeX directory, but I cannot find updmap. Exiting..."
			exit 1
		fi

		for thashes in `find /$TTEKDIR -name 'texhash'`;
		do
			if [ -n "`file $thashes | sed '/executable/!d;'`" ]; then
				TEXHASHLOC=$thashes
				break
			fi
		done
		
		if [ -z "$TEXHASHLOC" ]; then
			echo "You have a teTeX directory, but I cannot find texhash. Exiting..."
			exit 1
		fi
		
		#cut off last part
		TEXHASHLOC=`echo $TEXHASHLOC | sed s:/texhash::g`
		UPDLOC=`echo $UPDLOC | sed s:/updmap-sys::g | sed s:/updmap::g`
		
		#fix path
		PATH=$UPDLOC:$TEXHASHLOC:/usr/local/bin:$PATH
	else
		echo "You do not have teTeX at /usr/local/teTeX . Exiting..."
		exit 1
	fi
	
	if [ -n "`uname -a | sed '/5\.8/!d;'`" ]; then
		#Solaris 8
		TEMPLOCAL="usr/local/teTeX/share/texmf.local"
		TEMPOS="solaris8"
	elif [ -n "`uname -a | sed '/5\.9/!d;'`" ]; then
		#Solaris 9
		TEMPLOCAL="usr/local/teTeX/share/texmf-local"
		TEMPOS="solaris9"
	else
		echo "This package is only for Solaris 8 and 9."
		exit 1
	fi

export TEMPLOCAL;
export TEMPMF;
export TEMPOS;
export PATH;
export TTEKDIR;
export UPDLOC;
export TEXHASHLOC;

#run texhash
	#echo "Solaris 9"
	if [ -f $TEXHASHLOC/texhash ]; then
		$TEXHASHLOC/texhash
	fi

#finish up
	#echo "Solaris 9"
	if [ -f $UPDLOC/updmap-sys ]; then
		$UPDLOC/updmap-sys --enable Map bera.map --quiet >/dev/null 2>/dev/null
		sleep 3
		$UPDLOC/updmap-sys --quiet >/dev/null 2>/dev/null
	elif [ -f $UPDLOC/updmap ]; then
		$UPDLOC/updmap --enable Map bera.map --quiet >/dev/null 2>/dev/null
		sleep 3
		$UPDLOC/updmap --quiet >/dev/null 2>/dev/null
	fi
exit 0

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc Instructions pers.cfg.example
%doc /%{mloc}/doc/*
/%{mloc}/tex/generic/rutgers/*
/%{mloc}/tex/latex/bera/*
/%{mloc}/tex/latex/rutgers/*
/%{mloc}/tex/rutgers/*
/%{mloc}/fonts/vf/public/bera/*
/%{mloc}/fonts/map/vtex/bera.ali
/%{mloc}/fonts/map/dvips/bera.map
/%{mloc}/fonts/type1/public/bera/*
/%{mloc}/fonts/tfm/public/bera/*
/%{mloc}/fonts/afm/public/bera/*
/%{mtex}/dvips/config/bera.map
/%{mloc}/misc/updmap.patch

%changelog
* Thu Jul 17 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.1-2
- Added some docs
* Tue Jul 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1-1
- Updated to version 1.1
- This version contains some changes I made in order to comply with the Rutgers Identity people
* Sat Nov 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0-2
- Fixed some small issues
