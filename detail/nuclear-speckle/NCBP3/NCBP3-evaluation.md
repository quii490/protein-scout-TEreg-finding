---
type: protein-evaluation
gene: "NCBP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCBP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCBP3 / C17orf85 |
| 蛋白名称 | Nuclear cap-binding protein subunit 3 |
| 蛋白大小 | 620 aa / 70.6 kDa |
| UniProt ID | Q53F19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 620 aa / 70.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 8BY6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019416, IPR012677; Pfam: PF10309 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear cap binding complex (GO:0005846)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- RNA cap binding complex (GO:0034518)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf85 |

**关键文献**:
1. NCBP3 positively impacts mRNA biogenesis.. *Nucleic acids research*. PMID: 32960271
2. Structural basis for competitive binding of productive and degradative co-transcriptional effectors to the nuclear cap-binding complex.. *Cell reports*. PMID: 38175753
3. NCBP3: A Multifaceted Adaptive Regulator of Gene Expression.. *Trends in biochemical sciences*. PMID: 33032857
4. Structural basis for the synergistic assembly of the snRNA export complex.. *Nature structural & molecular biology*. PMID: 40610714
5. The alternative cap-binding complex is required for antiviral defense in vivo.. *PLoS pathogens*. PMID: 31856218

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.8% |
| 中等置信 (pLDDT 50-70) 占比 | 22.3% |
| 低置信 (pLDDT<50) 占比 | 39.2% |
| 有序区域 (pLDDT>70) 占比 | 38.5% |
| 可用 PDB 条目 | 8BY6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 38.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019416, IPR012677; Pfam: PF10309 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCBP1 | 0.996 | 0.829 | — |
| NCBP2 | 0.986 | 0.619 | — |
| EIF4E | 0.928 | 0.000 | — |
| THOC2 | 0.916 | 0.702 | — |
| AGO2 | 0.915 | 0.000 | — |
| ZC3H11A | 0.913 | 0.776 | — |
| EIF4E2 | 0.912 | 0.000 | — |
| RAMAC | 0.910 | 0.000 | — |
| RNMT | 0.905 | 0.000 | — |
| DDX39B | 0.890 | 0.788 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000373657.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | doi:10.1093/nar/gkaa743|pubmed |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| EBI-1788056 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| GDI2 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| RAB5C | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| THOC7 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| EIF4A3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| THOC1 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 8BY6 | pLDDT=62.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NCBP3 — Nuclear cap-binding protein subunit 3，非常新颖，仅有少数基础研究。
2. 蛋白大小620 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53F19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074356-NCBP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCBP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53F19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
