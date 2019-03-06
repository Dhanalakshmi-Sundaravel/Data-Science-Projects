% WRITE YOU CODE HERE!!! 
% marking id = 2623
function [NEvec, EValue] = myPCA(DS)
   CDS = cov(DS);
   
   [Evec,EValue]=eig(CDS);
   
   NEValue=diag(EValue);
   SortedEValue = sort(NEValue,'descend');
   [row,col] = size(Evec);
  % disp(Evec);
   NEvec = zeros(row,col);
   for i = 1:length(NEValue)
       NEvec(:,i)=Evec(:,find(NEValue==SortedEValue(i))); 
   end
  % disp(NEvec);
end