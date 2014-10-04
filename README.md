pylink
======

Link python model and RTL simulation.


���Y�̃v���W�F�N�g�̃��C�Z���X��GPLV2�ł��B���p��킸�t���[�ŗ��p�ł��܂����A�ύX�E�C��������Ȃ��Ɋւ�炸�ĔЕz����ꍇ�͂��̃v���W�F�N�g�̃R�[�h���܂�ł��邱�Ƃ𖾋L���A�\�[�X�R�[�h��S�ĊJ������`��������܂��B�܂��A���̃R�[�h�𗘗p�������Ƃɂ��󂯂����Q�̐Ӗ��𒘍�҂͕����܂���B�ڍׂ�LICENSE���������������B


�g�p���邽�߂̏����F

�ꉞ�S���t���[�ő�������悤�ɂ��Ă��܂�(Windows�ȊO)�B�ȉ��͒��҂����������ł����A����verilog�V�~�����[�^��Python�̃o�[�W�����ł��R�[�h���͓̂��삷��Ǝv���܂��Bmake�̎菇�͕ς��Ǝv���܂����B

OS:
Windows 7

Python:
ver2.7���g�p���Ă��܂��B

numpy,scipy:
2014.10.04���_�ł̍ŐV�ł��g�p

verilog simulator:
Modelsim Altera STARTER EDITION 10.1e


�\���̐���:

python file:

pylink.py:
�M���̔����ƃA�i���O���̃��f�������s���A�^�C���h���u���ŃV�~�����[�g���Ă��܂��B�f�[�^�̋L�^�Ȃǂ��s���܂��B
backend.py:
�f�[�^�̓ǂݍ��݁A�O���t�̕\���A�N���X���ւɂ��x���Z�o���s���Ă��܂��B

C file:

call_python_class.c:
PythonAPI�ɂ��python�N���X�A�֐����ĂԂ��߂̃��b�p�[�ł��B

system verilog file:
top.sv
DPI-C�^�X�N���Ăяo��top���W���[����AD�M�����������郂�W���[��sinc_filter���܂�ł��܂��B

�g����:
������̏ꍇ�����ʂ�backend.py�����s������Adata�f�B���N�g���̃t�@�C���������肵�Ċm�F���܂��B

python�P�̂̏ꍇ:
pylink.py��main�����s���Ă��������B

c����Ăяo��:
call_class_python.c�����L�̂悤�ɃR���p�C�����Ď��s���Ă��������B

>>>gcc .\call_python_class.c -I C:\Python27\include -L C:\Python27\libs -lpython27 -o call_python_class
>>>call_class

verilog simulator�ŁF
�X�}�[�g�Ȏ菇�Ƃ͎v���܂��񂪁A�A�A
���悢���@������΋����Ă��������B

modelsim�ɂāAtop.sv���R���p�C�����Ă��������B
�����Ĉȉ��̃R�}���h��modelsim��œ��͂��Adll�쐬�ɕK�v�ȃt�@�C����f���o�����܂��B
>>>vlog -novopt -dpiheader dpiheader.h top.sv
>>>vsim top -dpiexportobj cexports.obj -c
windows�̃R�}���h�v�����v�g����A�ȉ������s���Adll���쐬���Ă��������B
>>>gcc -c -g -I C:\Python27\include -L C:\Python27\libs -lpython27 call_python_class.c -o call_python_class.obj
>>>gcc -shared -I C:\Python27\include -L C:\Python27\libs -o cimports.dll call_python_class.obj cexports.obj C:\altera\14.0\modelsim_ase\win32aloem\mtipli.dll -lpython27

�����܂ł�dll�쐬�Bdll���ł�����A�Ă�modelsim�ɖ߂�A
>>>vsim -c -sv_lib cimports top -do "add wave -r /*;run -all;quit -sim"
���Ă��������B

���ς̃R�c:
dll�̕ύX���ł��邾�����炷(=.c�t�@�C����ҏW���Ȃ�)�̂��R�c�ł��B
dll���ł߂��python�͍ăR���p�C������K�v�Ȃ��A���ς��邱�Ƃ��o���܂��B
.sv�������ς��ꍇ��dll�͍ăR���p�C������K�v������܂���B
DPI-C�������ς��ꍇ��dll���ăR���p�C���K�v���o�Ă��܂��B

Python,C,systemverilog�̂ǂꂪ�����������킩��Ȃ��Ȃ�����Averilog simulator�őS�ē����ɓ������̂ł͂Ȃ��APython�����œ���������AC-Python�œ��������肵�Ă݂Ă��悢�Ǝv���܂��B

C-Python�œ������ꍇ��Python�����̉��ςł���΃R���p�C���͕K�v����܂���B


����
2014.10.04:�Ƃ肠���������łƂ��Č��J���܂����B�F�X�ƕs���͂���܂����A���w�E����������΍K���ł��B