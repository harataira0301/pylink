pylink
======

Link python model and RTL simulation.

###�{�v���W�F�N�g�̖ړI:
scipy,numpy�ɑ�\�����L�x�ȉȊw�Z�p�v�Z�����I�[�v���\�[�X���C�u����������Python���ADPI-C�o�R��RTL���؊�����@�����Ƃɂ��APython�ŋL�q���ꂽ�A�i���O��H�╨�����f����RTL�ŋL�q���ꂽ�f�W�^����H����s���ăV�~�����[�V�������邱�Ƃ��ړI�ł��B���f�����ɂ����Fast SPICE�n�V�~�����[�^��荂���ɃV�X�e�����x���V�~�����[�V�������s���܂��B���ʂ͂���Ȋ�����

<a target="_blank"
    href="./result.PNG">
    <img style="max-width:100%;" alt="my image"
        src="/mino0123/image/raw/master/my_image.png">
</a>

###�g�p���邽�߂̏����F
���s���͑S�ăt���[�ő�������悤�ɂ��Ă��܂�(Windows�ȊO)�B�ȉ��͒��҂����������ł����A����verilog�V�~�����[�^��Python�̃o�[�W�����ł��R�[�h���͓̂��삷��Ǝv���܂��Bmake�̎菇�͕ς��Ǝv���܂����B

OS:
Windows 7

Python:
ver2.7���g�p���Ă��܂��B

numpy,scipy,matplotlib:
2014.10.04���_�ł̍ŐV�ł��g�p

verilog simulator:
Modelsim Altera STARTER EDITION 10.1e


###�\��:

Python�t�@�C��:
pylink.py:
�M���̔���(����g+�����gsin�g)�ƃA�i���O��(�A�i���O�t�B���^�[+�f���^�V�O�}AD)�̃��f�������s���A�^�C���h���u���ŃV�~�����[�g���Ă��܂��B�Ԃ�l�̓f���^�V�O�}�̏o�͒l�ł��B�V�~�����[�V�����Ɠ����Ƀf�[�^�̋L�^���s���܂��B�܂����L��verilog���܂�sinc�t�B���^�[�Ɠ����̃t�B���^�[�̃��f�����܂ނ��߁A���ʂ�RTL�Ɣ�r���邱�Ƃ��o���܂��B���͂Ȃ����኱���ʂ��Ⴄ�̂ŁA�������������Ă���Ƃ���ł��΁B
backend.py:
�f�[�^�̓ǂݍ��݁A�O���t�̕\���A�N���X���ւɂ��x���Z�o���s���Ă��܂��B

C�t�@�C��:
call_python_class.c:
PythonAPI�ɂ��python�N���X�A�֐����ĂԂ��߂̃��b�p�[�ł��B

systemverilog�t�@�C��:
top.sv
DPI-C�^�X�N���Ăяo��top���W���[����AD�M�����������郂�W���[��sinc_filter���܂�ł��܂��B

###�g����:
�@Python�P�́A�AC-Python�A�Bverilog simulator-C-Python�̎O�̊��Ŏ��s�ł��܂��B
�@�A�̏ꍇ�ARTL����̌��ʂ̓[���Ƃ݂Ȃ���f�[�^�Ɋi�[����܂��B
������̏ꍇ�����ʂ�backend.py�����s���Ċm�F���܂��B

Python�P�̂̏ꍇ:
pylink.py��main�����s���Ă��������B

c-Python�Ŏ��s:
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


###���ς̃R�c:
dll�̕ύX���ł��邾�����炷(=.c�t�@�C����ҏW���Ȃ�)�̂��R�c�ł��B
dll���ł߂�΍ăR���p�C������K�v�Ȃ��APython�͉��ς��邱�Ƃ��o���܂��B
.sv�������ς��ꍇ��dll�͍ăR���p�C������K�v������܂���B
DPI-C�������ς��ꍇ��dll���ăR���p�C���K�v���o�Ă��܂��B

Python,C,systemverilog�̂ǂ��������������킩��Ȃ��Ȃ�����Averilog simulator�őS�ē����ɓ������̂ł͂Ȃ��APython�����œ���������AC-Python�œ��������肵�Ă݂Ă��悢�Ǝv���܂��B

###���C�Z���X�F
���̃v���W�F�N�gGPLV2�Ń��C�Z���X���Ă��܂��B���p�񏤗p��킸�t���[�ŗ��p�ł��܂����A�ύX�E�C���̂���Ȃ��Ɋւ�炸�ĔЕz����ꍇ�͂��̃v���W�F�N�g�̃R�[�h���܂�ł��邱�Ƃ𖾋L���A�v��������ꍇ�̓\�[�X�R�[�h��S�ĊJ������`��������܂��B�܂��A���̃R�[�h�𗘗p�������Ƃɂ��󂯂����Q�̐Ӗ��𒘍�҂͕����܂���B�ڍׂ�LICENSE���������������B

###����
2014.10.04:�Ƃ肠���������łƂ��Č��J���܂����B�s��������܂�����Anannyakannya@gmail.com���w�E����������΍K���ł��B

###�Ō�ɁF
���̃v���W�F�N�g��2014/10/3 Design solution forum�ɂ����ĊJ�Â��ꂽsystemverilog�n�b�J�\���ɂ����ĊJ�����ꂽ���̂ł��B���f���[�^��@vengineer�l�ADesign solution forum�^�c�̊F�l�A���̑����x�������������F�l�ɂ��̏���؂�Ă���\���グ�܂��B
