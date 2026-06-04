---
type: protein-evaluation
gene: "SYCE1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYCE1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SYCE1 / bA108K14.6|CT76 |
| 蛋白全称 | Synaptonemal complex central element protein 1 |
| 蛋白大小 | 351 aa |
| UniProt ID | Q8N0S2 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE1/IF_images/K-562_1.jpg|K-562]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 351 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 66 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 2 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.0** | UniProt + GO 核定位互证 (+1) |
|  | **原始总分** |  | **101/183** | **100.0/183** |  |  |  |
|  | **归一化总分** |  | **55.2/100** | **54.6/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Chromosome | 实验证据/预测 |
| GO-CC | GO:0005634 | IEA |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 351 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 66 |

**评价**: PubMed 66 篇，中等研究热度

**关键文献**:
1. França MM & Mendonca BB (2022). "Genetics of ovarian insufficiency and defects of folliculogenesis". *Best Pract Res Clin Endocrinol Metab*. PMID: 34794894
2. Feng K et al. (2022). "Novel exon mutation in SYCE1 gene is associated with non-obstructive azoospermia". *J Cell Mol Med*. PMID: 35023261
3. Dunne OM & Davies OR (2019). "Molecular structure of human synaptonemal complex protein SYCE1". *Chromosoma*. PMID: 30607510
4. Huang Y et al. (2022). "Novel copy number variations within SYCE1 caused meiotic arrest and non-obstructive azoospermia". *BMC Med Genomics*. PMID: 35718780
5. Sánchez-Sáez F et al. (2020). "Meiotic chromosome synapsis depends on multivalent SYCE1-SIX6OS1 interactions that are disrupted in cases of human infertility". *Sci Adv*. PMID: 32917591
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 351 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 2 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE1/SYCE1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | SYCE1 |
| Pfam | SYCE1 |

**染色质调控潜力分析**: 2 domain(s), 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:synaptonemal complex (GO:0000795, IBA:GO_Central)
- P:synaptonemal complex assembly (GO:0007130, IC:BHF-UCL)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 2 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
**总计**: +1.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 66 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SYCE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171772-SYCE1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SYCE1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8N0S2
- STRING: https://string-db.org/network/9606.ENSG00000171772
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N0S2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SYCE1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/SYCE1/SYCE1-PAE.png]]




