---
type: protein-evaluation
gene: "ECEL1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ECEL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ECEL1 / XCE, DINE |
| 蛋白名称 | Endothelin-converting enzyme-like 1 |
| UniProt ID | O95672 |
| 蛋白大小 | 775 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA Nucleoplasm + UniProt Membrane (不一致) |
| 蛋白大小 | 10/10 | ×1 | 10 | 775 aa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 35 篇 (21-50) |
| 三维结构 | 8/10 | ×3 | 24 | AF pLDDT=87.8, good=88%, 无PDB |
| 调控结构域 | 7/10 | ×2 | 14 | Peptidase M13 家族, 无明确DNA结合域 |
| PPI 网络 | 3/10 | ×3 = 9 | STRING 20 partners, 低置信度, 非调控 |
| 互证加分 | — | max +3 | +0.5 | AF高质量 + GO Membrane一致 |
| **原始总分** |  |  | **125.5/183** |  |
| **归一化总分** |  |  | **68.6/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 6 | Tier1 |
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Membrane | Reviewed |
| GO-Cellular Component | Plasma membrane | TAS |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ECEL1/IF_images/168393_A_8_3_rna_selected.jpg|HPA IF]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ECEL1/IF_images/168393_A_8_4_rna_selected.jpg|HPA IF]]

**结论**: HPA 显示核质定位，但 UniProt 和 GO 均注释为膜蛋白。存在定位不一致。作为金属蛋白酶家族成员，膜定位更符合其酶功能。核定位证据需进一步验证。

#### 3.2 蛋白大小评估
**评价**: 775 aa，处于理想范围（200-800 aa），适合生化实验。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 35 |
| 主要研究方向 | 神经发育, 金属蛋白酶, 先天性关节挛缩 |

**主要研究方向**:
- 内皮素转换酶家族成员，参与神经肽加工
- 与先天性远端关节挛缩症相关 (DA5D)

**关键文献**:
1. Dieterich et al. (2013). "ECEL1 mutation in arthrogryposis". PMID: 23261301
2. Kiryu-Seo et al. (2000). "ECEL1 in neuronal development". PMID: 10686356
3. Valdenaire et al. (2000). "XCE characterization". PMID: 10764113

**评价**: 研究非常少（35篇），主要集中在神经发育和酶功能。新颖性极高。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 87.8 |
| 有序区域 (pLDDT>70) 占比 | 88% |
| 可用 PDB 条目 | 无 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ECEL1/ECEL1-PAE.png]]

**PAE 数值分析**:
- AF 预测质量高（mean pLDDT=87.8），88%残基高置信度
- 无实验 PDB 结构，仅有预测
- 极高的折叠域置信度提示结构域预测可靠

**评价**: AF 预测质量好，但无实验结构验证。金属蛋白酶折叠域可信度极高。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | Peptidase M13 (IPR018497) |
| InterPro | Peptidase M13, N-terminal (IPR008753) |
| InterPro | Peptidase M13, C-terminal (IPR024079) |
| Pfam | Peptidase M13 |

**染色质调控潜力分析**: 无已知的 DNA 结合或染色质调控结构域。蛋白为金属蛋白酶，主要功能为肽键水解。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| CHRND | 0.62 | 乙酰胆碱受体 | 否 |
| RPS12 | 0.55 | 核糖体蛋白 | 否 |
| PIEZO2 | 0.50 | 机械敏感通道 | 否 |

**已知复合体成员** (GO Cellular Component):
- Plasma membrane (GO:0005886)

**PPI 互证分析**:
- STRING 邻居主要为膜受体、核糖体蛋白
- 调控相关比例: 0/20 (0%)

**评价**: PPI 网络缺乏转录调控相关伙伴，符合金属蛋白酶功能定位。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AF pLDDT 87.8 | 高质量预测 | 是 |
| 结构域 | InterPro/Pfam | Peptidase M13 | 一致 |
| 定位 | HPA Nucleoplasm vs UniProt Membrane | 不一致 | 否 |

**互证加分明细**:
- AF 预测质量高 (+0.5)
- **总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: 2 / 5

**核心优势**:
1. 研究极度新颖（35篇）
2. AF 结构质量好

**风险/不确定性**:
1. 定位不一致：HPA核 vs UniProt膜
2. 无DNA结合/染色质调控结构域
3. PPI 网络不富集调控因子

**下一步建议**:
- [ ] 独立验证核定位（IF/细胞组分分离）
- [ ] 确认核定位是否为其真实功能定位

### 5. 数据来源
- UniProt: O95672 (https://www.uniprot.org/uniprotkb/O95672)
- AlphaFold: AF-O95672-F1 v6 (https://alphafold.ebi.ac.uk/entry/O95672)
- Protein Atlas: ECEL1 (https://www.proteinatlas.org/)
- PubMed: ECEL1 (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: ECEL1 (https://string-db.org/)
- InterPro: O95672 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ECEL1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ECEL1/ECEL1-PAE.png]]




