Summary:	Script to make and update /dev entries
Summary(de):	Script zum Erstellen und Aktualisieren von /dev-Einträgen
Summary(fr):	Script pour créer et mettre à jour les entrées /dev
Summary(pl):	Skrypt do tworzenia i poprawiania urz±dzeñ z /dev
Summary(tr):	Aygýt tanýmý yapmak ve deðiþtirmek için bir araç
Name:		MAKEDEV
Version:	2.6
Release:	4
License:	FRS - Freely Redistributable Software
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5: f809a62a47ac46ad2b13354aa57c3ed0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/dev

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a script
which makes it easier to create and maintain the files which fill the
/dev tree.

%description -l de
Die /dev-Hierarchie enthält spezielle Dateien, von denen jede einem
Hardwaregerättyp entspricht, der von Linux unterstützt wird. Dieses
Paket enthält ein Skript, das die Erstellung und die Pflege der
Dateien innerhalb dieser Hierarchie vereinfacht.

%description -l fr
L'arborescence /dev contient des fichiers spéciaux. Chacun d'eux
correspond à un périphérique matériel gérable par Linux. Ce paquetage
contient un script facilitant la création et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl
Pliki specjalne znajduj±ce siê w katalogu /dev odpowiadaj±
urz±dzeniom, które s± obs³ugiwane przez Linuksa. Pakiet ten zawiera
skrypt, który uczyni tworzenie i operowanie tymi plikami ³atwiejszym.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya
baðlý aygýtlarý göstermek için özel dosyalar kullanýrlar. Bu özel
dosyalarýn tümü /dev dizin yapýsý altýndadýr. Bu paket en çok
kullanýlan /dev dosyalarýný içerir. Bu dosyalar, bir sistemin düzgün
olarak iþleyebilmesi için temel gereksinimlerdendir.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%{_mandir}/man8/*
