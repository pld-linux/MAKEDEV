Summary:     	Script to make and update /dev entries
Summary(fr): 	Script pour créer et mettre à jour les entrées /dev
Summary(tr): 	Aygýt tanýmý yapmak ve deðiþtirmek için bir araç
Summary(pl): 	Skrypt do tworzenia i poprawiania urz±dzeñ z /dev 
Summary(de): 	Script zum Erstellen und Aktualisieren von /dev-Einträgen
Name:        	MAKEDEV
Version:     	2.6
Release:     	1
Copyright:   	none
Group:       	Utilities/System
Group(pl):   	Narzêdzia/System
Source:      	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_bindir		/dev

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

make install \
	ROOT=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%{_mandir}/man8/*

%changelog
* Thu Jun 10 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>

- prepared v. 2.6 for PLD Linux
  (based most on debian MAKEDEV)
- perm of /dev/MAKEDEV changed to standard 644 root.root

* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5-2]
- now package is FHS 2.0 compliant.

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
