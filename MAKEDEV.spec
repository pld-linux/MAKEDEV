Summary:     	Script to make and update /dev entries
Summary(fr): 	Script pour créer et mettre à jour les entrées /dev
Summary(tr): 	Aygýt tanýmý yapmak ve deðiþtirmek için bir araç
Summary(pl): 	Skrypt do tworzenia i poprawiania urz±dzeñ z /dev 
Summary(de): 	Script zum Erstellen und Aktualisieren von /dev-Einträgen
Name:        	MAKEDEV
Version:     	2.5
Release:     	3
Copyright:   	none
Group:       	Utilities/System
Group(pl):   	Narzêdzia/System
Source:      	ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.tar.gz
Requires:    	fileutils 
Requires:	setup
BuildArch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a script
which makes it easier to create and maintain the files which fill the
/dev tree.

%description -l de
Die /dev-Hierarchie enthält spezielle Dateien, von denen jede einem 
Hardwaregerättyp entspricht, der von Linux unterstützt wird. Dieses 
Paket enthält ein Skript, das die Erstellung und die Pflege der Dateien
innerhalb dieser Hierarchie vereinfacht. 

%description -l fr
L'arborescence /dev contient des fichiers spéciaux. Chacun d'eux
correspond à un périphérique matériel gérable par Linux. Ce paquetage
contient un script facilitant la création et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl
Pliki specjalne znajduj±ce siê w katalogu /dev odpowiadaj± urz±dzeniom,
które s± obs³ugiwane przez Linuxa. Pakiet ten zawiera skrypt, który
uczyni tworzenie i operowanie tymi plikami ³atwiejszym.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya baðlý
aygýtlarý göstermek için özel dosyalar kullanýrlar. Bu özel dosyalarýn tümü
/dev dizin yapýsý altýndadýr. Bu paket en çok kullanýlan /dev dosyalarýný
içerir. Bu dosyalar, bir sistemin düzgün olarak iþleyebilmesi için temel
gereksinimlerdendir.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{dev,usr/share/man/man8}

make install \
	ROOT=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT/usr/share/man

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(744,root,root) /dev/MAKEDEV
/usr/share/man/man8/*

%changelog
* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5-2]
- now package is FHS 2.0 compliat.

* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [2.3.1-9]
- added gzipping man page
- added Group(pl)
- cosmetic changes

* Mon Sep  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.3.1-8]
- removed %post wit adding floppy grouup (it is by default in setup),
- changed permission to 744 on /dev/MAKEDEV,
- added using %%{name} and %%{version} macros in Buildroot and Source.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Jun 29 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Apr 23 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, tr

* Thu Apr 23 1998 Erik Troan <ewt@redhat.com>
- fixed group add script (had -r instead of -o)

* Fri Apr 17 1998 Erik Troan <ewt@redhat.com>
- put -o option on groupadd after -g -- I hope Christian can tell me why

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- redirect groupadd call so that we're more quiet

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- 2.3.1: use /usr/sbin/groupadd from new shadow utils

* Mon Sep 29 1997 Michael K. Johnson <johnsonm@redhat.com>
- Updated to 2.3, as Nick agreed to me making an interim release while
  he figures out whether he wants to be the maintainer.

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- added dependencies
