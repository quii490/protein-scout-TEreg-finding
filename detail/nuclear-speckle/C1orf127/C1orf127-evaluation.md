---
type: protein-evaluation
gene: "C1orf127"
uniprot: "Q8N9H9"
date: 2026-06-28
tags: [protein-scout, nuclear-speckle, evaluation, rejected]
status: rejected
---

## C1orf127 / CIROZ 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | C1orf127 (现用名: CIROZ) |
| 蛋白全称 | Ciliated left-right organizer ZP-N domains-containing protein |
| UniProt ID | Q8N9H9 (Swiss-Prot, reviewed) |
| 蛋白大小 | 823 aa |
| UniProt 证据等级 | 1: Evidence at protein level |
| 亚细胞定位 | **Secreted** (分泌蛋白) |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | Secreted (UniProt); 细胞核定位无证据 |
| 蛋白大小 | 10/10 | x1 | 10.0 | 823 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=7; 左右不对称发育关键基因 |
| 三维结构 | 3/10 | x3 | 9.0 | pLDDT=52.66; 61%残基 pLDDT<50 |
| 调控结构域 | 2/10 | x2 | 4.0 | ZP-N domain; 无已知染色质/DNA结合域 |
| PPI | 2/10 | x3 | 6.0 | PPI degree=3 (PPI数据中实际连接极少) |
| **加权总分** | | | **69.0/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

**核定位: 不成立 (FAIL)**。CIROZ 是一个**分泌蛋白**，UniProt 明确标注 "Secreted"，含信号肽(1-22 aa)，功能为左右不对称发育的胞外信号分子。HPA 标注 "Cytosol; Nuclear speckles" 可能为抗体交叉反应或过表达伪影，与 UniProt Swiss-Prot 的 curated 定位矛盾。此蛋白不具备核定位信号，不存在于细胞核中。

**功能**: 在胚胎发育中调控左右不对称体轴建立。CIROZ 致病突变导致常染色体隐性内脏异位症 14 型 (HTX14)。作为分泌型胞外蛋白参与 Nodal 信号通路。

**结构**: AlphaFold 预测质量差 (pLDDT=52.66)，61% 残基置信度极低，提示蛋白高度无序。ZP-N 结构域见于许多分泌蛋白和膜蛋白，与染色质调控无关。

**文献**: 7 篇 PubMed 文献，全部围绕左右不对称发育和先天性心脏病，无一篇涉及转录调控或染色质。

### 4. 总体评价
**38.3/100** | **REJECTED**

**拒绝理由**: CIROZ 是一个**分泌蛋白**，功能为胚胎左右不对称发育信号分子。HPA 标注的 "Nuclear speckles" 定位与 UniProt Swiss-Prot curated 定位 "Secreted" 直接矛盾。该蛋白不含任何 DNA 结合域、染色质调控域或核定位信号，不具备任何作为 TE 调控因子的生物学基础。属于 HPA 假阳性导致的误分类。

**关键文献**:
- 39753129: CIROZ is dispensable in ancestral vertebrates but essential for left-right patterning in humans
- 40030011: Recessive genetic contribution to congenital heart disease in 5,424 probands
