
# Git 常用操作与问题解决指南

## 一、基础操作

### 1. 初始化仓库
```bash
git init
```

### 2. 配置用户信息
```bash
git config user.name "你的名字"
git config user.email "你的邮箱"
```

### 3. 查看状态
```bash
git status
```

### 4. 添加文件到暂存区
```bash
# 添加单个文件
git add filename

# 添加所有文件
git add .
```

### 5. 提交更改
```bash
git commit -m "提交信息"
```

### 6. 查看提交历史
```bash
# 简洁显示
git log --oneline

# 图形化显示
git log --oneline --graph

# 详细显示
git log
```

---

## 二、分支操作

### 1. 查看分支
```bash
# 查看本地分支
git branch

# 查看所有分支（包括远程）
git branch -a
```

### 2. 创建分支
```bash
git branch 分支名
```

### 3. 切换分支
```bash
git checkout 分支名
```

### 4. 创建并切换到新分支
```bash
git checkout -b 分支名
```

### 5. 合并分支
```bash
# 先切换到目标分支（如 master）
git checkout master

# 合并指定分支
git merge 分支名
```

### 6. 删除分支
```bash
# 删除已合并的分支
git branch -d 分支名

# 强制删除分支（即使未合并）
git branch -D 分支名
```

---

## 三、合并冲突解决

### 冲突表现
当 Git 无法自动合并时，会在文件中显示如下标记：
```
<<<<<<< HEAD
当前分支的内容
=======
要合并分支的内容
>>>>>>> 分支名
```

### 解决步骤
1. 打开冲突文件
2. 删除标记符（`<<<<<<<`, `=======`, `>>>>>>>`）
3. 手动编辑保留需要的内容
4. 添加文件并提交：
```bash
git add 冲突文件
git commit -m "解决合并冲突"
```

---

## 四、常见问题与解决方案

### 问题1：提交后发现错误，想修改最后一次提交
**解决方案：**
```bash
# 修改文件后
git add 文件名
git commit --amend -m "新的提交信息"
```

### 问题2：想撤销暂存区的文件
**解决方案：**
```bash
git reset HEAD 文件名
```

### 问题3：想丢弃工作区的修改
**解决方案：**
```bash
git checkout -- 文件名
```

### 问题4：想回退到某个历史版本
**解决方案：**
```bash
# 查看历史提交获取 commit ID
git log --oneline

# 回退到指定版本（保留更改在工作区）
git reset --soft commitID

# 回退到指定版本（保留更改在暂存区）
git reset --mixed commitID

# 回退到指定版本（丢弃所有更改）
git reset --hard commitID
```

### 问题5：提交信息写错了
**解决方案：**
```bash
# 修改最后一次提交信息
git commit --amend -m "正确的提交信息"
```

### 问题6：想查看某个文件的修改历史
**解决方案：**
```bash
git log --oneline 文件名
```

### 问题7：想查看某次提交的具体修改
**解决方案：**
```bash
git show commitID
```

---

## 五、其他实用命令

### 1. 查看差异
```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与上次提交的差异
git diff --cached

# 查看工作区与上次提交的差异
git diff HEAD
```

### 2. 暂存当前工作（保存但不提交）
```bash
# 暂存工作
git stash

# 查看暂存列表
git stash list

# 恢复最近的暂存
git stash pop

# 删除某个暂存
git stash drop stash@{n}
```

### 3. 查看远程仓库
```bash
git remote -v
```

### 4. 添加远程仓库
```bash
git remote add origin 远程仓库地址
```

### 5. 重命名主分支（GitHub 默认使用 main）
```bash
git branch -M main
```

### 6. 推送到远程仓库
```bash
# 首次推送（设置上游分支）
git push -u origin main

# 后续推送
git push origin main
```

### 7. 从远程拉取最新代码
```bash
git pull origin main
```

### 8. 克隆远程仓库到本地
```bash
git clone 远程仓库地址
```

---

## 六、最佳实践建议

1. **频繁提交**：小步快跑，保持提交粒度适中
2. **清晰的提交信息**：使用有意义的提交信息
3. **合理使用分支**：功能开发在分支上进行，稳定后再合并到 master
4. **经常同步**：频繁从远程拉取最新代码
5. **及时解决冲突**：遇到冲突不要害怕，仔细分析后解决

---

## 七、GitHub 远程仓库完整操作流程

### 准备工作
1. 在 GitHub 上注册账号
2. 创建新的远程仓库（不要添加任何文件）

### 完整步骤

#### 1. 连接本地仓库与远程仓库
```bash
# 查看当前远程仓库
git remote -v

# 添加远程仓库
git remote add origin https://github.com/用户名/仓库名.git
```

#### 2. 重命名主分支（GitHub 推荐使用 main）
```bash
git branch -M main
```

#### 3. 推送到远程仓库
```bash
# 首次推送（设置上游分支）
git push -u origin main
```

#### 4. 后续同步操作
```bash
# 拉取远程最新代码
git pull origin main

# 推送本地提交
git push origin main
```

---

## 八、在本项目中的实践

我们在这个项目中已经演示了：
- ✅ Git 初始化与配置
- ✅ 文件添加与提交
- ✅ 分支创建与切换
- ✅ 分支合并与冲突解决
- ✅ 修改最后一次提交
- ✅ **连接并推送到 GitHub 远程仓库**（最新完成！）

本项目已成功推送到：https://github.com/GXiaokang/git-learning-project.git

你可以继续在这个项目中尝试其他 Git 命令来加深理解！
