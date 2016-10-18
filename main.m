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
game_data = py.matlab_starter.getGameData();

%% process data

n = size(game_data,2);
uid = zeros(n,1);
summary = zeros(n,4);
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
    summary(i,:) = [double(gd.unique_id), double(it.invest), double(it.winning), double(it.money)];
    
    % % self.analyzer.insert_result(self.winning, self.invest, self.money + self.winning)
    r = it.result_dict;
    % % self.analyzer.insert_operation(operation, option, ticket_odds, invest, market_odds, changing_rate)
    o = it.operation_list;
    
    r_struct = struct(r);
    summary_result_cell{i} = r_struct;
    
    o_cell = cell(o);
    summary_operation_cell{i} = o_cell;
    
end

%% data analysis
format long g;
sum_summary = sum(summary);

% display firt 10 games:
disp(summary(1:10,:));

% show sum
disp(sum_summary);

