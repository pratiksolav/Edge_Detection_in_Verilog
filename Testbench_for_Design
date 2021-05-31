module tss_tb;
reg CLK,BUS_CON,STROBE_DATA,STROBE_MODE,RESET;
wire [7:0]IN_VAL;
wire [7:0]BUS;
reg [7:0]OUT_VAL;
reg OUT_VALID;
test_just_2 T1(.clk(CLK),.bus(BUS),.bus_con(BUS_CON),.strobe_data(STROBE_DATA),.strobe_mode(STROBE_MODE),.reset(RESET));
assign IN_VAL =BUS;
assign BUS = (OUT_VALID==1'b1)? OUT_VAL : 8'hZZ;
initial begin 
CLK=0;
forever
#5 CLK=~CLK;
end
initial begin
RESET=0;
#10
RESET=1;
//Take auto generated testbench
// The output generated from the Python File responsible for converting Raw Image into Pixel Data
$finish;
end
endmodule
