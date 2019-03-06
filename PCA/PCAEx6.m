% WRITE YOU CODE HERE!!!_
% marking id = 2623
  X = load("pcadata.mat");
 %disp(X.X);
 
 scatter(X.X(:,1),X.X(:,2))
 xlim([0 7]);
 ylim([2 8]);
 [Xmu,mu]=subtractMean(X.X);
 
 [U,S]=myPCA(Xmu);
 disp(U(:,1));
 PCA1 = U(:,1)'+mu;
 PCA2 = U(:,2)'+mu;
 
 %U(:,2)=U(:,2)+mu(1,2);
 hold on
 line([mu(1,1) PCA1(1,1)],[mu(1,2) PCA1(1,2)],'Color','red');
 line([mu(1,1) PCA2(1,1)],[mu(1,2) PCA2(1,2)],'Color','green');
 
 hold off

 
 K = 1;
 Z = projectData(Xmu,U,K);
 
 disp(Z(1:3,:));
 
 Xrec = recoverData(Z, U, K, mu);
 scatter(X.X(:,1),X.X(:,2))
 xlim([0 7]);
 ylim([2 8]);
 hold on
 scatter(Xrec(:,1),Xrec(:,2),'r','*');
 hold off
 
%Part 2
 X = load("pcafaces.mat");
 
 displayData(X.X(1:100,:));
 [Xmu,mu]=subtractMean(X.X);
 [U,S]=myPCA(Xmu);

 U=mu+U;
 K = 1;
 Z = projectData(Xmu,U,K);
 
 Xrec = recoverData(Z, U, K, mu);
 subplot(1,2,1)
 displayData(X.X(1:100,:));
 subplot(1,2,2)
 displayData(Xrec(1:100,:));
