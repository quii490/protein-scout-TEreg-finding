---
type: protein-evaluation
gene: "DAG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAG1 — REJECTED (研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAG1 |
| 蛋白名称 | Dystroglycan 1 |
| 蛋白大小 | 895 aa / 97.4 kDa |
| UniProt ID | Q14118 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Vesicles, Plasma membrane; 额外: Nucleoplasm; UniProt: Secreted, extracellular space; Secreted, extracellular space |
| 蛋白大小 | 8/10 | x1 | 8 | 895 aa / 97.4 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 1EG4, 2MK7, 5GGP, 5LLK, 6JJY, 7E9K, 7E9L |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR027468, IPR041631, IPR006644, IPR015919, IPR008 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Secreted, extracellular space; Secreted, extracellular space, extracellular matrix, basement membran... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- basement membrane (GO:0005604)
- basolateral plasma membrane (GO:0016323)
- contractile ring (GO:0070938)
- costamere (GO:0043034)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 569 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic variations and clinical spectrum of dystroglycanopathy in a large cohort of Chinese patients.. *Clinical genetics*. PMID: 33200426
2. Molecular Diagnosis of Limb-Girdle Muscular Dystrophy Using Next-Generation Sequencing Panels.. *Molecular syndromology*. PMID: 38357257
3. Identification of Sp1 and GC-boxes as transcriptional regulators of mouse Dag1 gene promoter.. *American journal of physiology. Cell physiology*. PMID: 19657058
4. The Dof protein DAG1 mediates PIL5 activity on seed germination by negatively regulating GA biosynthetic gene AtGA3ox1.. *The Plant journal : for cell and molecular biology*. PMID: 19874540
5. Expert panel curation of 31 genes in relation to limb girdle muscular dystrophy.. *Annals of clinical and translational neurology*. PMID: 39215466

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 38.0% |
| 有序区域 (pLDDT>70) 占比 | 52.1% |
| 可用 PDB 条目 | 1EG4, 2MK7, 5GGP, 5LLK, 6JJY, 7E9K, 7E9L, 8UF4 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 52.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027468, IPR041631, IPR006644, IPR015919, IPR008465; Pfam: PF18424, PF05454, PF05345 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTRN | 0.999 | 0.768 | — |
| LAMA2 | 0.999 | 0.311 | — |
| AGRN | 0.999 | 0.428 | — |
| DMD | 0.999 | 0.783 | — |
| SGCA | 0.999 | 0.193 | — |
| HSPG2 | 0.999 | 0.241 | — |
| SGCD | 0.999 | 0.311 | — |
| SSPN | 0.999 | 0.000 | — |
| NRXN1 | 0.998 | 0.000 | — |
| NRXN2 | 0.997 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 1EG4, 2MK7, 5GGP, 5LLK, 6JJY,  | pLDDT=68.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted, extracellular space; Secreted, extracell / Vesicles, Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DAG1 -- Dystroglycan 1，研究基础较多，新颖性有限。
2. 蛋白大小895 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 107 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14118
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173402-DAG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14118
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
