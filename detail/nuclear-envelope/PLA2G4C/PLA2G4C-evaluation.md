---
type: protein-evaluation
gene: "PLA2G4C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLA2G4C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLA2G4C |
| 蛋白名称 | Cytosolic phospholipase A2 gamma |
| 蛋白大小 | 541 aa / 60.9 kDa |
| UniProt ID | Q9UP65 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; UniProt: Cell membrane; Endoplasmic reticulum membrane; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 541 aa / 60.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016035, IPR002642; Pfam: PF01735 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cell membrane; Endoplasmic reticulum membrane; Mitochondrion membrane; Lipid droplet | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- lipid droplet (GO:0005811)
- membrane (GO:0016020)
- mitochondrial membrane (GO:0031966)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. An association between PLA2G6 and PLA2G4C gene polymorphisms and schizophrenia risk and illness severity in a Croatian population.. *Prostaglandins, leukotrienes, and essential fatty acids*. PMID: 28651698
2. Prognostic significance of PLA2G4C gene polymorphism in patients with stage II colorectal cancer.. *Acta oncologica (Stockholm, Sweden)*. PMID: 26364726
3. Primate-specific evolution of noncoding element insertion into PLA2G4C and human preterm birth.. *BMC medical genomics*. PMID: 21184677
4. Polymorphisms in PLA2G6 and PLA2G4C genes for calcium-independent phospholipase A2 do not contribute to attenuated niacin skin flush response in schizophrenia patients.. *Prostaglandins, leukotrienes, and essential fatty acids*. PMID: 26160611
5. Molecular-genetic pathways of hepatitis C virus regulation of the expression of cellular factors PREB and PLA2G4C, which play an important role in virus replication.. *Vavilovskii zhurnal genetiki i selektsii*. PMID: 38213698

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 15.0% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.0，有序区 80.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016035, IPR002642; Pfam: PF01735 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLCG2 | 0.912 | 0.000 | — |
| PLA2G2A | 0.910 | 0.000 | — |
| MAPK3 | 0.907 | 0.000 | — |
| MAPK1 | 0.906 | 0.000 | — |
| GNAS | 0.903 | 0.000 | — |
| PLCG1 | 0.902 | 0.000 | — |
| GNAQ | 0.900 | 0.000 | — |
| PLA2G7 | 0.803 | 0.000 | — |
| PNPLA6 | 0.796 | 0.000 | — |
| PLA2G15 | 0.793 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| Q9UG68 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 无 | pLDDT=84.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Endoplasmic reticulum membrane; Mit / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLA2G4C — Cytosolic phospholipase A2 gamma，非常新颖，仅有少数基础研究。
2. 蛋白大小541 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UP65
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105499-PLA2G4C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLA2G4C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UP65
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
