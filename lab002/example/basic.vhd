-- Libraries imports
library ieee;
use ieee.std_logic_1164.all;

-- Module interface description
entity my_module is
    port(
  	    clk : in std_logic;
  	    o   : out std_logic
    );
end entity;

-- Module architecture description
architecture rtl of my_module is
   signal d : std_logic;
   signal q : std_logic;
begin
	-- Combinatorial logic
	o <= q;
	d <= not q;
	
	-- Synchronous logic
    process(clk)
    begin
        if rising_edge(clk) then
            d <= q
        end if;
    end process

end rtl;
