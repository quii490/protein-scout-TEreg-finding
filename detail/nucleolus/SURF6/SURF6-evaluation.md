---
type: protein-evaluation
gene: "SURF6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SURF6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SURF6 / SURF-6 |
| 蛋白名称 | Surfeit locus protein 6 |
| 蛋白大小 | 361 aa / 41.5 kDa |
| UniProt ID | O75683 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 41.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.8; PDB: 8FKP, 8FKQ, 8FKR, 8FKS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029190, IPR007019; Pfam: PF04935 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic chromosome | Enhanced |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- granular component (GO:0001652)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SURF-6 |

**关键文献**:
1. Human nucleolar protein SURF6/RRP14 participates in early steps of pre-rRNA processing.. *PloS one*. PMID: 37450438
2. Implication of nucleolar protein SURF6 in ribosome biogenesis and preimplantation mouse development.. *Biology of reproduction*. PMID: 16855206
3. Granular component sub-phases direct ribosome biogenesis in the nucleolus.. *bioRxiv : the preprint server for biology*. PMID: 40093048
4. The human Surfeit locus.. *Genomics*. PMID: 9740673
5. Therapeutic targets for endometriosis: Genome-wide Mendelian randomization and colocalization analyses.. *Gene*. PMID: 37931855

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 22.7% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 25.2% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 8FKP, 8FKQ, 8FKR, 8FKS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8FKP, 8FKQ, 8FKR, 8FKS）+ AlphaFold高质量预测（pLDDT=73.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029190, IPR007019; Pfam: PF04935 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EBNA1BP2 | 0.991 | 0.688 | — |
| RRP15 | 0.982 | 0.577 | — |
| NIFK | 0.978 | 0.834 | — |
| GTPBP4 | 0.974 | 0.851 | — |
| RPF1 | 0.974 | 0.808 | — |
| MAK16 | 0.974 | 0.739 | — |
| BRIX1 | 0.960 | 0.776 | — |
| RSL24D1 | 0.956 | 0.579 | — |
| RPF2 | 0.956 | 0.227 | — |
| RRS1 | 0.949 | 0.596 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cwc25 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MRG15 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ND-B22 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| SMAD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| VDAC1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| COX15 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| PDHA1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 8FKP, 8FKQ, 8FKR, 8FKS | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus / Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Mitotic c | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SURF6 — Surfeit locus protein 6，非常新颖，仅有少数基础研究。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75683
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148296-SURF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SURF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75683
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
