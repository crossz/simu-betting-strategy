function [ output_args, output_sum ] = segmental_analysis( input_args, slice_size )
%SEGMENTAL_ANALYSIS 此处显示有关此函数的摘要
%   此处显示详细说明

summary = input_args;
% slice_size = 10;


numTaps = floor( size(summary,1) / slice_size );
slice_summary = cell(numTaps,1);
slice_sum = cell(numTaps,1);
    for tap = 1:numTaps
        idx_last_right = (tap-1) * slice_size;  % last element in previous tap
        idx_left = idx_last_right + 1;
        idx_right = idx_left + slice_size - 1;

        if idx_last_right <= size(summary,1)
            slice = summary(idx_left:idx_right, :);
            slice_summary{tap} = slice;
        end
        
        slice_sum{tap} = sum(slice);
        
    end
    
    
    output_args = slice_summary; 
    output_sum = slice_sum;
    
end

