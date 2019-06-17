% % Problem 1
% man2 = man;
% 
% % man2 = [800, 1200, 3];
% 
% for i = 1:800
%     for j = 1:1200
%         man2(i, j, 1) = man(i, j, 1)/3 + man(i, j, 2)/3 + man(i, j, 3)/3;
%         man2(i, j, 2) = man(i, j, 1)/3 + man(i, j, 2)/3 + man(i, j, 3)/3;
%         man2(i, j, 3) = man(i, j, 1)/3 + man(i, j, 2)/3 + man(i, j, 3)/3;
% %         fprintf('R: %d, G: %d, B: %d\n', man2(i, j, 1), man2(i, j, 2), man2(i, j, 3));
%     end
% end
% 
% % imshow(man)
% imshow(man2, [])

% % Problem 2
% man2 = [800, 1200, 3];
% im2double(man2);
% 
% for i = 1:800
%     for j = 1:1200
%         man2(i, j, 1) = sqrt(double((man(i, j, 1))^2)+(double(man(i, j, 2))^2)+(double(man(i, j, 3))^2))/sqrt(3*(255^2));
%         man2(i, j, 2) = man2(i, j, 1);
%         man2(i, j, 3) = man2(i, j, 1);
%         fprintf('R: %d, G: %d, B: %d\n', man2(i, j, 1), man2(i, j, 2), man2(i, j, 3));
%     end
% end
% 
% imshow(man2)

% Problem 4
% rgb yellow 255, 255, 0
WIT = [1330, 2000, 3];
% WIT = WIT2;
acceptable_distance = 70;
red =   170;
green = 170;
blue =  0;
im2double(WIT);
for i = 1:1330
    for j = 1:2000
        %grey
        WIT(i, j, 1) = sqrt(double((WIT2(i, j, 1))^2)+(double(WIT2(i, j, 2))^2)+(double(WIT2(i, j, 3))^2))/sqrt(3*(255^2));
        WIT(i, j, 2) = WIT(i, j, 1);
        WIT(i, j, 3) = WIT(i, j, 1);
        if sqrt(double(WIT2(i, j, 1)-red)^2+double(WIT2(i, j, 2)-green)^2+double(WIT(i, j, 3)-blue)^2) > acceptable_distance
            %Old Yella
            WIT(i, j, 1) = 255;
            WIT(i, j, 2) = 255;
            WIT(i, j, 3) = 0;
        end
    end
end
subplot(1, 2, 1);
imshow(WIT2)
subplot(1, 2, 2);
imshow(WIT);