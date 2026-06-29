---
title: "NEWS.txt 知识梳理"
type: doc-notes
date: 2026-06-27
tags: [文档/知识梳理]
source: "G:\转录\328.短剧 AI漫剧超暴力快速起号新技术\AI漫剧课程\Index-TTS2_ZZDH\Index-TTS2_ZZDH\venv\Lib\idlelib\NEWS.txt"
---

# NEWS.txt 知识梳理

> 来源: `NEWS.txt` | 字数: 54192

## 内容全文

What's New in IDLE 3.10.z

after 3.10.0 until 3.10.10?

Released 2023-04-03?

=========================

gh-97527: Fix a bug in the previous bugfix that caused IDLE to not

start when run with 3.10.8, 3.12.0a1, and at least Microsoft Python

3.10.2288.0 installed without the Lib/test package.  3.11.0 was never

affected.

gh-65802: Document handling of extensions in Save As dialogs.

gh-95191: Include prompts when saving Shell (interactive input/output).

gh-95511: Fix the Shell context menu copy-with-prompts bug of copying

an extra line when one selects whole lines.

gh-95471: Tweak Edit menu. Move 'Select All' above 'Cut' as it is used

with 'Cut' and 'Copy' but not 'Paste'.  Add a separator between 'Replace'

and 'Go to Line' to help IDLE issue triagers.

gh-95411: Enable using IDLE's module browser with .pyw files.

gh-89610: Add .pyi as a recognized extension for IDLE on macOS.  This allows

opening stub files by double clicking on them in the Finder.

bpo-28950: Apply IDLE syntax highlighting to `.pyi` files.  Add util.py

for common components.  Patch by Alex Waygood and Terry Jan Reedy.

bpo-46630: Make query dialogs on Windows start with a cursor in the

entry box.

bpo-46591: Make the IDLE doc URL on the About IDLE dialog clickable.

bpo-45296: Clarify close, quit, and exit in IDLE.  In the File menu,

'Close' and 'Exit' are now 'Close Window' (the current one) and 'Exit'

is now 'Exit IDLE' (by closing all windows).  In Shell, 'quit()' and

'exit()' mean 'close Shell'.  If there are no other windows,

this also exits IDLE.

bpo-45495: Add context keywords 'case' and 'match' to completions list.

bpo-45296: On Windows, change exit/quit message to suggest Ctrl-D, which

works, instead of <Ctrl-Z Return>, which does not work in IDLE.

What's New in IDLE 3.10.0

(since 3.9.0)

Released on 2021-10-04

=========================

bpo-45193: Make completion boxes appear on Ubuntu again.

bpo-40128: Mostly fix completions on macOS when not using tcl/tk 8.6.11

(as with 3.9).

bpo-33962: Move the indent space setting from the Font tab to the new Windows

tab. Patch by Mark Roseman and Terry Jan Reedy.

bpo-40468: Split the settings dialog General tab into Windows and Shell/Ed

tabs. Move help sources, which extend the Help menu, to the Extensions tab.

Make space for new options and shorten the dialog. The latter makes the

dialog better fit small screens.

bpo-44010: Highlight the new match statement's soft keywords: match, case,

and _. This highlighting is not perfect and will be incorrect in some rare

cases, especially for some _s in case patterns.

bpo-44026: Include interpreter's typo fix suggestions in message line

for NameErrors and AttributeErrors.  Patch by E. Paine.

bpo-41611: Avoid occasional uncaught exceptions and freezing when using

completions on macOS.

bpo-37903: Add mouse actions to the shell sidebar.  Left click and

optional drag selects one or more lines of text, as with the

editor line number sidebar.  Right click after selecting text lines

displays a context menu with 'copy with prompts'.  This zips together

prompts from the sidebar with lines from the selected text.  This option

also appears on the context menu for the text.

bpo-43981: Fix reference leaks in test_sidebar and test_squeezer.

Patches by Terry Jan Reedy and Pablo Galindo

bpo-37892: Change Shell input indents from tabs to spaces.  Shell input

now 'looks right'.  Making this feasible motivated the shell sidebar.

bpo-37903: Move the Shell input prompt to a side bar.

bpo-43655: Make window managers on macOS and X Window recognize

IDLE dialog windows as dialogs.

bpo-42225: Document that IDLE can fail on Unix either from misconfigured IP

masquerade rules or failure displaying complex colored (non-ascii) characters.

bpo-43283: Document why printing to IDLE's Shell is often slower than

printing to a system terminal and that it can be made faster by

pre-formatting a single string before printing.

bpo-23544: Disable Debug=>Stack Viewer when user code is running or

Debugger is active, to prevent hang or crash.  Patch by Zackery Spytz.

bpo-43008: Make IDLE invoke :func:`sys.excepthook` in normal,

2-process mode.  User hooks were previously ignored.

Patch by Ken Hilton.

bpo-33065: Fix problem debugging user classes with __repr__ method.

bpo-32631: Finish zzdummy example extension module: make menu entries

work; add docstrings and tests with 100% coverage.

bpo-42508: Keep IDLE running on macOS.  Remove obsolete workaround

that prevented running files with shortcuts when using new universal2

installers built on macOS 11.

bpo-42426: Fix reporting offset of the RE error in searchengine.

bpo-42416: Display docstrings in IDLE calltips in more cases,

by using inspect.getdoc.

bpo-33987: Mostly finish using ttk widgets, mainly for editor,

settings, and searches.  Some patches by Mark Roseman.

bpo-40511: Stop unnecessary "flashing" when typing opening and closing

parentheses inside the parentheses of a function call.

bpo-38439: Add a 256x256 pixel IDLE icon to the Windows .ico file. Created by

Andrew Clover. Remove the low-color gif variations from the .ico file.

bpo-41775: Make 'IDLE Shell' the shell title.

bpo-35764: Rewrite the Calltips doc section.

bpo-40181: In calltips, stop reminding that '/' marks the end of

positional-only arguments.

What's New in IDLE 3.9.0 (since 3.8.0)

Released on 2020-10-05?

======================================

bpo-41468: Improve IDLE run crash error message (which users should

never see).

bpo-41373: Save files loaded with no line ending, as when blank, or

different line endings, by setting its line ending to the system

default. Fix regression in 3.8.4 and 3.9.0b4.

bpo-41300: Save files with non-ascii chars.  Fix regression in

3.9.0b4 and 3.8.4.

bpo-37765: Add keywords to module name completion list.  Rewrite

Completions section of IDLE doc.

bpo-41152: The encoding of ``stdin``, ``stdout`` and ``stderr`` in IDLE

is now always UTF-8.

bpo-41144: Make Open Module open a special module such as os.path.

bpo-40723: Make test_idle pass when run after import.

Patch by Florian Dahlitz.

bpo-38689: IDLE will no longer freeze when inspect.signature fails

when fetching a calltip.

bpo-27115: For 'Go to Line', use a Query entry box subclass with

IDLE standard behavior and improved error checking.

bpo-39885: When a context menu is invoked by right-clicking outside

of a selection, clear the selection and move the cursor.  Cut and

Copy require that the click be within the selection.

bpo-39852: Edit "Go to line" now clears any selection, preventing

accidental deletion.  It also updates Ln and Col on the status bar.

bpo-39781: Selecting code context lines no longer causes a jump.

bpo-39663: Add tests for pyparse find_good_parse_start().

bpo-39600: Remove duplicate font names from configuration list.

bpo-38792: Close a shell calltip if a :exc:`KeyboardInterrupt`

or shell restart occurs.  Patch by Zackery Spytz.

bpo-30780: Add remaining configdialog tests for buttons and

highlights and keys tabs.

bpo-39388: Settings dialog Cancel button cancels pending changes.

bpo-39050: Settings dialog Help button again displays help text.

bpo-32989: Add tests for editor newline_and_indent_event method.

Remove unneeded arguments and dead code from pyparse

find_good_parse_start method.

bpo-38943: Fix autocomplete windows not always appearing on some

systems.  Patch by Johnny Najera.

bpo-38944: Escape key now closes IDLE completion windows.  Patch by

Johnny Najera.

bpo-38862: 'Strip Trailing Whitespace' on the Format menu removes extra

newlines at the end of non-shell files.

bpo-38636: Fix IDLE Format menu tab toggle and file indent width. These

functions (default shortcuts Alt-T and Alt-U) were mistakenly disabled

in 3.7.5 and 3.8.0.

bpo-4630: Add an option to toggle IDLE's cursor blink for shell,

editor, and output windows.  See Settings, General, Window Preferences,

Cursor Blink.  Patch by Zackery Spytz.

bpo-26353: Stop adding newline when saving an IDLE shell window.

bpo-38598: Do not try to compile IDLE shell or output windows.

What's New in IDLE 3.8.0 (since 3.7.0)

Released on 2019-10-14

======================================

bpo-36698: IDLE no longer fails when writing non-encodable characters

to stderr.  It now escapes them with a backslash, like the regular

Python interpreter.  Add an errors field to the standard streams.

bpo-13153: Improve tkinter's handing of non-BMP (astral) unicode

characters, such as 'rocket \U0001f680'.  Whether a proper glyph or

replacement char is displayed depends on the OS and font.  For IDLE,

astral chars in code interfere with editing.

bpo-35379: When exiting IDLE, catch any AttributeError.  One happens

when EditorWindow.close is called twice.  Printing a traceback, when

IDLE is run from a terminal, is useless and annoying.

bpo-38183: To avoid test issues, test_idle ignores the user config

directory.  It no longer tries to create or access .idlerc or any files

within.  Users must run IDLE to discover problems with saving settings.

bpo-38077: IDLE no longer adds 'argv' to the user namespace when

initializing it.  This bug only affected 3.7.4 and 3.8.0b2 to 3.8.0b4.

bpo-38401: Shell restart lines now fill the window width, always start

with '=', and avoid wrapping unnecessarily. The line will still wrap

if the included file name is long relative to the width.

bpo-37092: Add mousewheel scrolling for IDLE module, path, and stack

browsers.  Patch by George Zhang.

bpo-35771: To avoid occasional spurious test_idle failures on slower

machines, increase the ``hover_delay`` in test_tooltip.

bpo-37824: Properly handle user input warnings in IDLE shell.

Cease turning SyntaxWarnings into SyntaxErrors.

bpo-37929: IDLE Settings dialog now closes properly when there is no

shell window.

bpo-37849: Fix completions list appearing too high or low when shown

above the current line.

bpo-36419: Refactor autocompete and improve testing.

bpo-37748: Reorder the Run menu.  Put the most common choice,

Run Module, at the top.

bpo-37692: Improve highlight config sample with example shell

interaction and better labels for shell elements.

bpo-37628: Settings dialog no longer expands with font size.

The font and highlight sample boxes gain scrollbars instead.

bpo-17535: Add optional line numbers for IDLE editor windows.

bpo-37627: Initialize the Customize Run dialog with the command line

arguments most recently entered before.  The user can optionally edit

before submitting them.

bpo-33610: Code context always shows the correct context when toggled on.

bpo-36390: Gather Format menu functions into format.py.  Combine

paragraph.py, rstrip.py, and format methods from editor.py.

bpo-37530: Optimize code context to reduce unneeded background activity.

Font and highlight changes now occur along with text changes instead

of after a random delay.

bpo-27452: Cleanup config.py by inlining RemoveFile and simplifying

the handling of __file__ in CreateConfigHandlers/

bpo-26806: To compensate for stack frames added by IDLE and avoid

possible problems with low recursion limits, add 30 to limits in the

user code execution process.  Subtract 30 when reporting recursion

limits to make this addition mostly transparent.

bpo-37325: Fix tab focus traversal order for help source and custom

run dialogs.

bpo-37321: Both subprocess connection error messages now refer to

the 'Startup failure' section of the IDLE doc.

bpo-37177: Properly attach search dialogs to their main window so

that they behave like other dialogs and do not get hidden behind

their main window.

bpo-37039: Adjust "Zoom Height" to individual screens by momentarily

maximizing the window on first use with a particular screen.  Changing

screen settings may invalidate the saved height.  While a window is

maximized, "Zoom Height" has no effect.

bpo-35763: Make calltip reminder about '/' meaning positional-only less

obtrusive by only adding it when there is room on the first line.

bpo-5680: Add 'Run Customized' to the Run menu to run a module with

customized settings. Any command line arguments entered are added

to sys.argv. One can suppress the normal Shell main module restart.

bpo-35610: Replace now redundant editor.context_use_ps1 with

.prompt_last_line.  This finishes change started in bpo-31858.

bpo-32411: Stop sorting dict created with desired line order.

bpo-37038: Make idlelib.run runnable; add test clause.

bpo-36958: Print any argument other than None or int passed to

SystemExit or sys.exit().

bpo-36807: When saving a file, call file.flush() and os.fsync()

so bits are flushed to e.g. a USB drive.

bpo-36429: Fix starting IDLE with pyshell.

Add idlelib.pyshell alias at top; remove pyshell alias at bottom.

Remove obsolete __name__=='__main__' command.

bpo-30348: Increase test coverage of idlelib.autocomplete by 30%.

Patch by Louie Lu.

bpo-23205: Add tests and refactor grep's findfiles.

bpo-36405: Use dict unpacking in idlelib.

bpo-36396: Remove fgBg param of idlelib.config.GetHighlight().

This param was only used twice and changed the return type.

bpo-23216: IDLE: Add docstrings to search modules.

bpo-36176: Fix IDLE autocomplete & calltip popup colors.

Prevent conflicts with Linux dark themes

(and slightly darken calltip background).

bpo-36152: Remove colorizer.ColorDelegator.close_when_done and the

corresponding argument of .close().  In IDLE, both have always been

None or False since 2007.

bpo-36096: Make colorizer state variables instance-only.

bpo-32129: Avoid blurry IDLE application icon on macOS with Tk 8.6.

Patch by Kevin Walzer.

bpo-24310: Document settings dialog font tab sample.

bpo-35689: Add docstrings and tests for colorizer.

bpo-35833: Revise IDLE doc for control codes sent to Shell.

Add a code example block.

bpo-35770: IDLE macosx deletes Options => Configure IDLE.

It previously deleted Window => Zoom Height by mistake.

(Zoom Height is now on the Options menu).  On Mac, the settings

dialog is accessed via Preferences on the IDLE menu.

bpo-35769: Change new file name from 'Untitled' to 'untitled'.

bpo-35660: Fix imports in window module.

bpo-35641: Properly format calltip for function without docstring.

bpo-33987: Use ttk Frame for ttk widgets.

bpo-34055: Fix erroneous 'smart' indents and newlines in IDLE Shell.

bpo-28097: Add Previous/Next History entries to Shell menu.

bpo-35591: Find Selection now works when selection not found.

bpo-35598: Update config_key: use PEP 8 names and ttk widgets,

make some objects global, and add tests.

bpo-35196: Speed up squeezer line counting.

bpo-35208: Squeezer now counts wrapped lines before newlines.

bpo-35555: Gray out Code Context menu entry when it's not applicable.

bpo-22703: Improve the Code Context and Zoom Height menu labels.

The Code Context menu label now toggles between Show/Hide Code Context.

The Zoom Height menu now toggles between Zoom/Restore Height.

Zoom Height has moved from the Window menu to the Options menu.

bpo-35521: Document the editor code context feature.

Add some internal references within the IDLE doc.

bpo-34864: When starting IDLE on MacOS, warn if the system setting

"Prefer tabs when opening documents" is "Always".  As previous

documented for this issue, running IDLE with this setting causes

problems.  If the setting is changed while IDLE is running,

there will be no warning until IDLE is restarted.

bpo-35213: Where appropriate, use 'macOS' in idlelib.

bpo-34864: Document two IDLE on MacOS issues.  The System Preferences

Dock "prefer tabs always" setting disables some IDLE features.

Menus are a bit different than as described for Windows and Linux.

bpo-35202: Remove unused imports in idlelib.

bpo-33000: Document that IDLE's shell has no line limit.

A program that runs indefinitely can overfill memory.

bpo-23220: Explain how IDLE's Shell displays output.

Add new subsection "User output in Shell".

bpo-35099: Improve the doc about IDLE running user code.

"IDLE -- console differences" is renamed "Running user code".

It mostly covers the implications of using custom sys.stdxxx objects.

bpo-35097: Add IDLE doc subsection explaining editor windows.

Topics include opening, title and status bars, .py* extension, and running.

Issue 35093: Document the IDLE document viewer in the IDLE doc.

Add a paragraph in "Help and preferences", "Help sources" subsection.

bpo-1529353: Explain Shell text squeezing in the IDLE doc.

bpo-35088: Update idlelib.help.copy_string docstring.

We now use git and backporting instead of hg and forward merging.

bpo-35087: Update idlelib help files for the current doc build.

The main change is the elimination of chapter-section numbers.

bpo-1529353: Output over N lines (50 by default) is squeezed down to a button.

N can be changed in the PyShell section of the General page of the

Settings dialog.  Fewer, but possibly extra long, lines can be squeezed by

right clicking on the output.  Squeezed output can be expanded in place

by double-clicking the button or into the clipboard or a separate window

by right-clicking the button.

bpo-34548: Use configured color theme for read-only text views.

bpo-33839: Refactor ToolTip and CallTip classes; add documentation

and tests.

bpo-34047: Fix mouse wheel scrolling direction on macOS.

bpo-34275: Make calltips always visible on Mac.

Patch by Kevin Walzer.

bpo-34120: Fix freezing after closing some dialogs on Mac.

This is one of multiple regressions from using newer tcl/tk.

bpo-33975: Avoid small type when running htests.

Since part of the purpose of human-viewed tests is to determine that

widgets look right, it is important that they look the same for

testing as when running IDLE.

bpo-33905: Add test for idlelib.stackview.StackBrowser.

bpo-33924: Change mainmenu.menudefs key 'windows' to 'window'.

Every other menudef key is the lowercase version of the

corresponding main menu entry (in this case, 'Window').

bpo-33906: Rename idlelib.windows as window

Match Window on the main menu and remove last plural module name.

Change imports, test, and attribute references to match new name.

bpo-33917: Fix and document idlelib/idle_test/template.py.

The revised file compiles, runs, and tests OK.  idle_test/README.txt

explains how to use it to create new IDLE test files.

bpo-33904: In rstrip module, rename class RstripExtension as Rstrip.

bpo-33907: For consistency and clarity, rename calltip objects.

Module calltips and its class CallTips are now calltip and Calltip.

In module calltip_w, class CallTip is now CalltipWindow.

bpo-33855: Minimally test all IDLE modules.

Standardize the test file format.  Add missing test files that import

the tested module and perform at least one test.  Check and record the

coverage of each test.

bpo-33856: Add 'help' to Shell's initial welcome message.

What's New in IDLE 3.7.0 (since 3.6.0)

Released on 2018-06-27

======================================

bpo-33656: On Windows, add API call saying that tk scales for DPI.

On Windows 8.1+ or 10, with DPI compatibility properties of the Python

binary unchanged, and a monitor resolution greater than 96 DPI, this

should make text and lines sharper and some colors brighter.

On other systems, it should have no effect.  If you have a custom theme,

you may want to adjust a color or two.  If perchance it make text worse

on your monitor, you can disable the ctypes.OleDLL call near the top of

pyshell.py and report the problem on python-list or idle-dev@python.org.

bpo-33768: Clicking on a context line moves that line to the top

of the editor window.

bpo-33763: Replace the code context label widget with a text widget.

bpo-33664: Scroll IDLE editor text by lines.

(Previously, the mouse wheel and scrollbar slider moved text by a fixed

number of pixels, resulting in partial lines at the top of the editor

box.)  This change also applies to the shell and grep output windows,

but currently not to read-only text views.

bpo-33679: Enable theme-specific color configuration for Code Context.

(Previously, there was one code context foreground and background font

color setting, default or custom, on the extensions tab, that applied

to all themes.)  For built-in themes, the foreground is the same as

normal text and the background is a contrasting gray.  Context colors for

custom themes are set on the Hightlights tab along with other colors.

When one starts IDLE from a console and loads a custom theme without

definitions for 'context', one will see a warning message on the

console.

bpo-33642: Display up to maxlines non-blank lines for Code Context.

If there is no current context, show a single blank line.  (Previously,

the Code Contex had numlines lines, usually with some blank.)  The use

of a new option, 'maxlines' (default 15), avoids possible interference

with user settings of the old option, 'numlines' (default 3).

bpo-33628: Cleanup codecontext.py and its test.

bpo-32831: Add docstrings and tests for codecontext.py.

Coverage is 100%.  Patch by Cheryl Sabella.

bpo-33564: Code context now recognizes async as a block opener.

bpo-21474: Update word/identifier definition from ascii to unicode.

In text and entry boxes, this affects selection by double-click,

movement left/right by control-left/right, and deletion left/right

by control-BACKSPACE/DEL.

bpo-33204: Consistently color invalid string prefixes.

A 'u' string prefix cannot be paired with either 'r' or 'f'.

IDLE now consistently colors as much of the prefix, starting at the

right, as is valid.  Revise and extend colorizer test.

bpo-32984: Set __file__ while running a startup file.

Like Python, IDLE optionally runs 1 startup file in the Shell window

before presenting the first interactive input prompt.  For IDLE,

option -s runs a file named in environmental variable IDLESTARTUP or

PYTHONSTARTUP; -r file runs file.  Python sets __file__ to the startup

file name before running the file and unsets it before the first

prompt.  IDLE now does the same when run normally, without the -n

option.

bpo-32940: Replace StringTranslatePseudoMapping with faster code.

bpo-32916: Change 'str' to 'code' in idlelib.pyparse and users.

bpo-32905: Remove unused code in pyparse module.

bpo-32874: IDLE - add pyparse tests with 97% coverage.

bpo-32837: IDLE - require encoding argument for textview.view_file.

Using the system and place-dependent default encoding for open()

is a bad idea for IDLE's system and location-independent files.

bpo-32826: Add "encoding=utf-8" to open() in IDLE's test_help_about.

GUI test test_file_buttons() only looks at initial ascii-only lines,

but failed on systems where open() defaults to 'ascii' because

readline() internally reads and decodes far enough ahead to encounter

a non-ascii character in CREDITS.txt.

bpo-32765: Update configdialog General tab create page docstring.

Add new widgets to the widget list.

bpo-32207: Improve tk event exception tracebacks in IDLE.

When tk event handling is driven by IDLE's run loop, a confusing

and distracting queue.EMPTY traceback context is no longer added

to tk event exception tracebacks.  The traceback is now the same

as when event handling is driven by user code.  Patch based on

a suggestion by Serhiy Storchaka.

bpo-32164: Delete unused file idlelib/tabbedpages.py.

Use of TabbedPageSet in configdialog was replaced by ttk.Notebook.

bpo-32100: Fix old and new bugs in pathbrowser; improve tests.

Patch mostly by Cheryl Sabella.

bpo-31860: The font sample in the settings dialog is now editable.

Edits persist while IDLE remains open.

Patch by Serhiy Storchake and Terry Jan Reedy.

bpo-31858: Restrict shell prompt manipulation to the shell.

Editor and output windows only see an empty last prompt line.  This

simplifies the code and fixes a minor bug when newline is inserted.

Sys.ps1, if present, is read on Shell start-up, but is not set or changed.

Patch by Terry Jan Reedy.

bpo-28603: Fix a TypeError that caused a shell restart when printing

a traceback that includes an exception that is unhashable.

Patch by Zane Bitter.

bpo-13802: Use non-Latin characters in the Font settings sample.

Even if one selects a font that defines a limited subset of the unicode

Basic Multilingual Plane, tcl/tk will use other fonts that define a

character.  The expanded example give users of non-Latin characters

a better idea of what they might see in the shell and editors.

To make room for the expanded sample, frames on the Font tab are

re-arranged.  The Font/Tabs help explains a bit about the additions.

Patch by Terry Jan Reedy

bpo-31460: Simplify the API of IDLE's Module Browser.

Passing a widget instead of an flist with a root widget opens the

option of creating a browser frame that is only part of a window.

Passing a full file name instead of pieces assumed to come from a

.py file opens the possibility of browsing python files that do not

end in .py.

bpo-31649: Make _htest and _utest parameters keyword-only.

These are used to adjust code for human and unit tests.

bpo-31459: Rename module browser from Class Browser to Module Browser.

The original module-level class and method browser became a module

browser, with the addition of module-level functions, years ago.

Nested classes and functions were added yesterday.  For back-

compatibility, the virtual event <<open-class-browser>>, which

appears on the Keys tab of the Settings dialog, is not changed.

Patch by Cheryl Sabella.

bpo-1612262: Module browser now shows nested classes and functions.

Original patches for code and tests by Guilherme Polo and

Cheryl Sabella, respectively.  Revisions by Terry Jan Reedy.

bpo-31500: Tk's default fonts now are scaled on HiDPI displays.

This affects all dialogs.  Patch by Serhiy Storchaka.

bpo-31493: Fix code context update and font update timers.

Canceling timers prevents a warning message when test_idle completes.

bpo-31488: Update non-key options in former extension classes.

When applying configdialog changes, call .reload for each feature class.

Change ParenMatch so updated options affect existing instances attached

to existing editor windows.

bpo-31477: Improve rstrip entry in IDLE doc.

Strip Trailing Whitespace strips more than blank spaces.

Multiline string literals are not skipped.

bpo-31480: fix tests to pass with zzdummy extension disabled. (#3590)

To see the example in action, enable it on options extensions tab.

bpo-31421: Document how IDLE runs tkinter programs.

IDLE calls tcl/tk update in the background in order to make live

interaction and experimentation with tkinter applications much easier.

bpo-31414: Fix tk entry box tests by deleting first.

Adding to an int entry is not the same as deleting and inserting

because int('') will fail.  Patch by Terry Jan Reedy.

bpo-27099: Convert IDLE's built-in 'extensions' to regular features.

About 10 IDLE features were implemented as supposedly optional

extensions.  Their different behavior could be confusing or worse for

users and not good for maintenance.  Hence the conversion.

The main difference for users is that user configurable key bindings

for builtin features are now handled uniformly.  Now, editing a binding

in a keyset only affects its value in the keyset.  All bindings are

defined together in the system-specific default keysets in config-

extensions.def.  All custom keysets are saved as a whole in config-

extension.cfg.  All take effect as soon as one clicks Apply or Ok.

The affected events are '<<force-open-completions>>',

'<<expand-word>>', '<<force-open-calltip>>', '<<flash-paren>>',

'<<format-paragraph>>', '<<run-module>>', '<<check-module>>', and

'<<zoom-height>>'.  Any (global) customizations made before 3.6.3 will

not affect their keyset-specific customization after 3.6.3. and vice

versa.

Initial patch by Charles Wohlganger, revised by Terry Jan Reedy.

bpo-31051:  Rearrange condigdialog General tab.

Sort non-Help options into Window (Shell+Editor) and Editor (only).

Leave room for the addition of new options.

Patch by Terry Jan Reedy.

bpo-30617: Add docstrings and tests for outwin subclass of editor.

Move some data and functions from the class to module level.

Patch by Cheryl Sabella.

bpo-31287: Do not modify tkinter.messagebox in test_configdialog.

Instead, mask it with an instance mock that can be deleted.

Patch by Terry Jan Reedy.

bpo-30781: Use ttk widgets in ConfigDialog pages.

These should especially look better on MacOSX.

Patches by Terry Jan Reedy and Cheryl Sabella.

bpo-31206: Factor HighPage(Frame) class from ConfigDialog.

Patch by Cheryl Sabella.

bp0-31001: Add tests for configdialog highlight tab.

Patch by Cheryl Sabella.

bpo-31205: Factor KeysPage(Frame) class from ConfigDialog.

The slightly modified tests continue to pass.


> [!tip] 共 930 段，以上显示前 500 段
