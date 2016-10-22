%% init environment
if count(py.sys.path,'') == 0
    insert(py.sys.path,int32(0),'');
end

if count(py.sys.path,'lib') == 0
    insert(py.sys.path,int32(0),'lib');
end

% % Doest work for reloading python scripts
clear classes;

mod_main = py.importlib.import_module('matlab_starter');
py.reload(mod_main);
mod_it = py.importlib.import_module('WhoScoreInvestor');
py.reload(mod_it);


% % test: python environment
py.matlab_starter.helloworld()

% % get data
game_data = py.matlab_starter.matlab_get_data();

%% process data

n = size(game_data,2);
uid = zeros(n,1);
summary = zeros(n,5);
summary_result_cell = cell(1,n);
summary_operation_cell = cell(1,n);
for i = 1:n
    gd_pylist = game_data(i);
    gd_cell = cell(gd_pylist);
    gd = gd_cell{1};
    
    
    
    
    
    it = py.matlab_starter.process_one_game(gd);
    
    
    
    
    
    
    % % data for analysis
    uid_i = double(gd.unique_id);
    uid(i) = uid_i;
    
    % % self.analyzer.insert_result(self.winning, self.invest, self.money + self.winning)
    r = it.result_dict;
    % % self.analyzer.insert_operation(operation, option, ticket_odds, invest, market_odds, changing_rate)
    o = it.operation_list;
    
    r_struct = struct(r);
    summary_result_cell{i} = r_struct;
    
    o_cell = cell(o);
    summary_operation_cell{i} = o_cell;

    
    % summary list
    co_ornot = size(o,2) == 6;    
    summary(i,:) = [double(gd.unique_id), double(it.invest), double(it.winning), double(it.money), co_ornot];
    
end

%% data analysis
format long g;

% total sum
sum_summary = sum(summary);
disp('## total summary: ');
disp(sum_summary);

% CO sum
ind_co = find(summary(:,5)==1);
sum_co = summary(ind_co,:);
disp('## CO summary: ');
disp(sum(sum_co));
ind_co_not = find(summary(:,5)==0);
sum_co_not = summary(ind_co_not,:);
disp('## No-CO summary: ');
disp(sum(sum_co_not));


%% segamental analysis
slice_size = 10; 
[slice_summary, slice_sum] = segmental_analysis(summary, slice_size);
[slice_summary_co, slice_sum_co] = segmental_analysis(sum_co, slice_size);
[slice_summary_co_not, slice_sum_co_not] = segmental_analysis(sum_co_not, slice_size);


% % 
if size(slice_sum_co, 1) ~= 0 && size(slice_sum_co_not, 1) ~= 0
    slice_sum_mat = cell2mat(slice_sum);
    slice_sum_mat = [slice_sum_mat, slice_sum_mat(:,3)./slice_sum_mat(:,2)];
    slice_sum_co_mat = cell2mat(slice_sum_co);
    slice_sum_co_mat = [slice_sum_co_mat, slice_sum_co_mat(:,3)./slice_sum_co_mat(:,2)];
    slice_sum_co_not_mat = cell2mat(slice_sum_co_not);
    slice_sum_co_not_mat = [slice_sum_co_not_mat, slice_sum_co_not_mat(:,3)./slice_sum_co_not_mat(:,2)];
end
