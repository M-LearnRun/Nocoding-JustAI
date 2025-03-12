m = 70;   % kg
  k = 0.25; % kg/s
  g = 9.81; % m/s^2
  v0 = 0; % m/s
  t = 0:0.1:100; % 0에서 100초까지 0.1초 간격의 시간 배열
   
  % 속도 계산
  v = (m * g / k) * (1 - exp(-k * t / m));
   
  % 높이 계산
  h = (m * g / k) * t + (m^2 * g / k^2) * exp(-k * t / m) - (m^2 * g / k^2);
   
  % 결과 그래프 그리기
  figure;
  subplot(2, 1, 1);
  plot(t, v);
  title('속도 v(t)');
  xlabel('시간 (초)');
  ylabel('속도 (m/s)');
   
  subplot(2, 1, 2);
  plot(t, h);
  title('높이 h(t)');
  xlabel('시간 (초)');
  ylabel('높이 (m)');
   
  % 속도와 높이의 결과 출력
  fprintf('시간\t속도(m/s)\t높이(m)\n');
  for i = 1:length(t)
      fprintf('%5.1f\t%10.4f\t%10.4f\n', t(i), v(i), h(i));
  end
