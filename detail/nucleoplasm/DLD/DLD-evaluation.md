---
type: protein-evaluation
gene: "DLD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLD — REJECTED (研究热度过高 (PubMed strict=1264，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLD / GCSL, LAD, PHE3 |
| 蛋白名称 | Dihydrolipoyl dehydrogenase, mitochondrial |
| 蛋白大小 | 509 aa / 54.2 kDa |
| UniProt ID | P09622 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm, Cytokinetic bridge, Primary c; UniProt: Mitochondrion matrix; Nucleus; Cell projection, cilium, flag |
| 蛋白大小 | 10/10 | ×1 | 10 | 509 aa / 54.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1264 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.0; PDB: 1ZMC, 1ZMD, 1ZY8, 2F5Z, 3RNM, 5J5Z, 5NHG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050151, IPR036188, IPR023753, IPR016156, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm, Cytokinetic bridge, Primary cilium, Principal piece | Approved |
| UniProt | Mitochondrion matrix; Nucleus; Cell projection, cilium, flagellum; Cytoplasmic vesicle, secretory ve... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal matrix (GO:0043159)
- branched-chain alpha-ketoacid dehydrogenase complex (GO:0160157)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- motile cilium (GO:0031514)
- nucleus (GO:0005634)
- oxoadipate dehydrogenase complex (GO:0160167)
- oxoglutarate dehydrogenase complex (GO:0045252)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1264 |
| PubMed broad count | 4361 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GCSL, LAD, PHE3 |

**关键文献**:
1. Spatial Metabolomics and Transcriptomics Reveal Metabolic Reprogramming and Cellular Interactions in Nasopharyngeal Carcinoma with High PD-1 Expression and Therapeutic Response.. *Theranostics*. PMID: 40083932
2. Dihydrolipoamide Dehydrogenase Deficiency.. **. PMID: 25032271
3. Lipoic acid biosynthesis defects.. *Journal of inherited metabolic disease*. PMID: 24777537
4. Prognostic Role of Cuproptosis-Related Gene after Intracerebral Hemorrhage in Mice.. *Cellular and molecular neurobiology*. PMID: 40402195
5. Identification of Key Fatty Acid Metabolism-Related Genes in Alzheimer's Disease.. *Molecular neurobiology*. PMID: 40108056

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.0 |
| 高置信度残基 (pLDDT>90) 占比 | 92.1% |
| 置信残基 (pLDDT 70-90) 占比 | 0.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 1ZMC, 1ZMD, 1ZY8, 2F5Z, 3RNM, 5J5Z, 5NHG, 6HG8, 6I4P, 6I4Q |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1ZMC, 1ZMD, 1ZY8, 2F5Z, 3RNM, 5J5Z, 5NHG, 6HG8, 6I4P, 6I4Q）+ AlphaFold极高置信度预测（pLDDT=94.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050151, IPR036188, IPR023753, IPR016156, IPR006258; Pfam: PF07992, PF02852 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCKDHA | 0.999 | 0.131 | — |
| DLST | 0.999 | 0.906 | — |
| PDHA1 | 0.999 | 0.825 | — |
| DBT | 0.999 | 0.964 | — |
| OGDH | 0.999 | 0.880 | — |
| DLAT | 0.999 | 0.909 | — |
| BCKDHB | 0.999 | 0.290 | — |
| PDHB | 0.999 | 0.907 | — |
| PDHX | 0.999 | 0.991 | — |
| PDHA2 | 0.998 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000390667.1 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-14543|pubmed:16263718 |
| Pms2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| DLD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| stck | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG6654 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PDHX | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-14543|pubmed:16263718 |
| rtcR | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| caiB | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| murG | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.0 + PDB: 1ZMC, 1ZMD, 1ZY8, 2F5Z, 3RNM,  | pLDDT=94.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix; Nucleus; Cell projection, ci / Mitochondria; 额外: Nucleoplasm, Cytokinetic bridge, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DLD — Dihydrolipoyl dehydrogenase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小509 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1264 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1264 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09622
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091140-DLD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09622
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
