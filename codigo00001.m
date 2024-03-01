% Defina as matrizes do sistema
A = [ -2 , 1; -1 , -2];
B = [1; 0];
C = [1 , 0];
D = 0;

% Calcule os polos e zeros
polos = eig ( A ) ;
zeros = tzero ( ss (A , B , C , D ) ) ;

% Exiba os resultados
disp ('Polos :') ;
disp ( polos ) ;
disp ('Zeros :') ;
disp ( zeros ) ;
