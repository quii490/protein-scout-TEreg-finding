---
type: protein-evaluation
gene: "TENT4B"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENT4B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TENT4B / TRF4-2|TUT3 |
| 蛋白全称 | Terminal nucleotidyltransferase 4B |
| 蛋白大小 | 572 aa |
| UniProt ID | Q8NDF8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TENT4B/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TENT4B/IF_images/A-431_1.jpg|A-431]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 572 aa，处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed 52 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 6 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **107/183** |  |
| **归一化总分** |  |  | **58.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus, Nucleus, nucleolus, Cytoplasm | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 572 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 52 |

**评价**: PubMed 52 篇，中等研究热度

**关键文献**:
1. Bokros M et al. (2024). "RNA tailing machinery drives amyloidogenic phase transition". *Proc Natl Acad Sci U S A*. PMID: 38805292
2. Nagpal N & Agarwal S (2025). "Extension of replicative lifespan by synthetic engineered telomerase RNA in patient induced pluripotent stem cells". *Nat Biomed Eng*. PMID: 40579489
3. Block TM et al. (2021). "Host RNA quality control as a hepatitis B antiviral target". *Antiviral Res*. PMID: 33242518
4. Shin J et al. (2022). "Oppositional poly(A) tail length regulation by FMRP and CPEB1". *RNA*. PMID: 35217597
5. Menezes MR et al. (2018). "3' RNA Uridylation in Epitranscriptomics, Gene Regulation, and Disease". *Front Mol Biosci*. PMID: 30057901
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 572 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TENT4B/TENT4B-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | MTPAP-like_central |
| InterPro | NT_sf |
| InterPro | PAP_assoc |
| InterPro | Trf4-like |
| Pfam | MTPAP-like_central |
| Pfam | PAP_assoc |

**染色质调控潜力分析**: 6 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| purF | two hybrid pooling approach | 20711500 | — | — |
| hsamir10a5p | clash | 23622248 | — | — |
| EBI-54261957 | clash | 23622248 | — | — |
| EBI-54262192 | clash | 23622248 | — | — |
| EBI-54263754 | clash | 23622248 | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:TRAMP complex (GO:0031499, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 52 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TENT4B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121274-TENT4B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22TENT4B%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q8NDF8
- STRING: https://string-db.org/network/9606.ENSG00000121274
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDF8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[TENT4B-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/TENT4B/TENT4B-PAE.png]]




