%% light & time setting
%meeting point and meeting time
syms x_p y_p z_p t0 
% time(sym)
t=0:t0/100:t0;
% light source
S=[-3,5,3];
% light in vector
v_i=[-1,0,-4];
% light in(sym)
L_i=S'+t.*v_i';
%% surface setting
%n vector
n=[0,0,1];
%a point on surface
p=[0,1,0];
%%  equation for surface
eqn1=(x_p-p(1))*n(1)+(y_p-p(2))*n(2)+(z_p-p(3))*n(3)==0;
%% meeting point calcular,
% the meeting point & the time on surface
eqn2=S'+t0*v_i'==[x_p;y_p;z_p];
[x_p,y_p,z_p,t0]=solve([eqn1,eqn2],[x_p,y_p,z_p,t0]);
p_m=double([x_p,y_p,z_p]);
% make n vector in meeting point, cause class(n) is sym, change to double,
% or will get error on mesh
%% plot n
L_n=subs(p_m'+t.*n');
plot3(L_n(1,:),L_n(2,:),L_n(3,:),'b');
hold on
%% mesh surface
syms X Y Z;
% setting size of surface s_size;
s_size=5;
% get unit Matrix
u=ones(s_size/0.1*2+1);
%[X,Y] = meshgrid(-s_size+(p_m(1)+p_m(2))/2:.5:s_size+(p_m(1)+p_m(2))/2);
X=[-s_size+p_m(1):0.1:s_size+p_m(1)].*u;
Y=[-s_size+p_m(2):0.1:s_size+p_m(2)]'.*u;
%eqn_1_plot=(X-p(1))*n(1)+(Y-p(2))*n(2)+(Z-p(3))*n(3)==0;
Z=((X-p(1)).*n(1)+(Y-p(2))*n(2)-p(3)*n(3))/-n(3);
mesh(X,Y,Z);
hold on
%% plot light_in
%change light_in to double
L_i=double(subs(L_i));
plot3(L_i(1,:),L_i(2,:),L_i(3,:),'r');
hold on
%% reflact
% calculate reflect vector v_r
syms x_r y_r z_r
eqn1= -v_i*n'==[x_r,y_r,z_r]*n';
eqn2= cross(-v_i+[x_r,y_r,z_r],n)==0;
[x_r,y_r,z_r]=solve([eqn1,eqn2],[x_r,y_r,z_r]);
%% plot light reflact
% calculate reflect light L_r
v_r=double([x_r,y_r,z_r]);
L_r=subs(p_m'+t.*v_r');
plot3(L_r(1,:),L_r(2,:),L_r(3,:),'g');
hold on
%% calculate light transmission
% refractive index
n_water=1.3330;
n_ice=1.306;
n_air=1;
%n1->in,n2->trans
n1=n_water;
n2=n_air;
% check speicial case
% n vector is equal with -v_i,directly trans
if isequal(n/n*n',-v_i/v_i*v_i')
    v_t=v_i;
else
    % n1<n2, nothing will happen
    if (n1<=n2)
        % get sin£¨theta1),sin(theta2),cos(theta1),cos(theta2)
        cos1=(-v_i)*n'/sqrt(v_i*v_i'*n*n');
        sin1=sqrt(1-cos1^2);
        sin2=n1*sin1/n2;
        cos2=sqrt(1-sin2^2);
        % 3 eqution to get v_t
        syms x_t y_t z_t;
        eqn1= [x_t,y_t,z_t]*cross(v_i,n')'==0
        eqn2= [x_t,y_t,z_t]*[x_t;y_t;z_t]==v_i*v_i'
        eqn3= [x_t,y_t,z_t]*(-n)'/sqrt([x_t,y_t,z_t]*[x_t;y_t;z_t]*(-n)*(-n)') == cos2
        eqn4= [x_t,y_t,z_t]*v_i'/sqrt(([x_t,y_t,z_t]*v_i')*([x_t,y_t,z_t]*v_i')')==1
        [x_t,y_t,z_t]=vpasolve([eqn1,eqn2,eqn3,eqn4],[x_t,y_t,z_t]);
        v_t=double([x_t,y_t,z_t]);
    else 
        %n1>n2, must calculation brust angel
        sin2=1;
        %maximal angel- brust angel
        sin1_b=n2*sin2/n1;
        cos1=(-v_i)*n'/sqrt(v_i*v_i'*n*n');
        sin1=sqrt(1-cos1^2);
        if(sin1>=sin1_b) 
            % only reflcetion
            v_t=[0,0,0];
        else
            % normal case 
            sin2=n1*sin1/n2;
            cos2=sqrt(1-sin2^2);
            % 3 eqution to get v_t
            syms x_t y_t z_t;
            eqn1= [x_t,y_t,z_t]*cross(v_i,n')'==0;
            eqn2= [x_t,y_t,z_t]*[x_t;y_t;z_t]==v_i*v_i';
            eqn3= [x_t,y_t,z_t]*(-n)'/sqrt([x_t,y_t,z_t]*[x_t;y_t;z_t]*(-n)*(-n)') == cos2;
            [x_t,y_t,z_t]=vpasolve([eqn1,eqn2,eqn3],[x_t,y_t,z_t]);
            v_t=double([x_t,y_t,z_t]);
        end
    end
end
%% plot transmisson 
L_t=subs(p_m'+t.*v_t');
plot3(L_t(1,:),L_t(2,:),L_t(3,:),'g');
hold on