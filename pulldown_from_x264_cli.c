static const char * const pulldown_names[] = { "none", "22", "32", "64", "double", "triple", "euro", 0 };

typedef struct
{
    int mod;
    uint8_t pattern[24];
    float fps_factor;
} cli_pulldown_t;

enum pulldown_type_e
{
    X264_PULLDOWN_22 = 1,
    X264_PULLDOWN_32,
    X264_PULLDOWN_64,
    X264_PULLDOWN_DOUBLE,
    X264_PULLDOWN_TRIPLE,
    X264_PULLDOWN_EURO
};

#define TB  PIC_STRUCT_TOP_BOTTOM
#define BT  PIC_STRUCT_BOTTOM_TOP
#define TBT PIC_STRUCT_TOP_BOTTOM_TOP
#define BTB PIC_STRUCT_BOTTOM_TOP_BOTTOM

static const cli_pulldown_t pulldown_values[] =
{
    [X264_PULLDOWN_22]     = {1,  {TB},                                   1.0},
    [X264_PULLDOWN_32]     = {4,  {TBT, BT, BTB, TB},                     1.25},
    [X264_PULLDOWN_64]     = {2,  {PIC_STRUCT_DOUBLE, PIC_STRUCT_TRIPLE}, 1.0},
    [X264_PULLDOWN_DOUBLE] = {1,  {PIC_STRUCT_DOUBLE},                    2.0},
    [X264_PULLDOWN_TRIPLE] = {1,  {PIC_STRUCT_TRIPLE},                    3.0},
    [X264_PULLDOWN_EURO]   = {24, {TBT, BT, BT, BT, BT, BT, BT, BT, BT, BT, BT, BT,
                                   BTB, TB, TB, TB, TB, TB, TB, TB, TB, TB, TB, TB}, 25.0/24.0}
};

#undef TB
#undef BT
#undef TBT
#undef BTB

// indexed by pic_struct enum
static const float pulldown_frame_duration[10] = { 0.0, 1, 0.5, 0.5, 1, 1, 1.5, 1.5, 2, 3 };

static int encode( x264_param_t *param, cli_opt_t *opt )

const cli_pulldown_t *pulldown = NULL; // shut up gcc

if( opt->i_pulldown && !param->b_vfr_input )
    {
        param->b_pulldown = 1;
        param->b_pic_struct = 1;
        pulldown = &pulldown_values[opt->i_pulldown];
        param->i_timebase_num = param->i_fps_den;
        FAIL_IF_ERROR2( fmod( param->i_fps_num * pulldown->fps_factor, 1 ),
                        "unsupported framerate for chosen pulldown\n" );
        param->i_timebase_den = param->i_fps_num * pulldown->fps_factor;
    }

 if( opt->i_pulldown && !param->b_vfr_input )
        {
            pic.i_pic_struct = pulldown->pattern[ i_frame % pulldown->mod ];
            pic.i_pts = (int64_t)( pulldown_pts + 0.5 );
            pulldown_pts += pulldown_frame_duration[pic.i_pic_struct];
        }
