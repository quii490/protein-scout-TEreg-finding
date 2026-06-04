---
type: protein-evaluation
gene: "IFFO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IFFO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IFFO1 / IFFO |
| 蛋白名称 | Non-homologous end joining factor IFFO1 |
| 蛋白大小 | 559 aa / 62.0 kDa |
| UniProt ID | Q0D2I5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Nucleus, nucleoplasm; Nucleus inner membrane; Nucle |
| 蛋白大小 | 10/10 | ×1 | 10 | 559 aa / 62.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 6ABO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Nucleus, nucleoplasm; Nucleus inner membrane; Nucleus matrix | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- intermediate filament (GO:0005882)
- nuclear inner membrane (GO:0005637)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IFFO |

**关键文献**:
1. The nucleoskeleton protein IFFO1 immobilizes broken DNA and suppresses chromosome translocation during tumorigenesis.. *Nature cell biology*. PMID: 31548606
2. Five Critical Gene-Based Biomarkers With Optimal Performance for Hepatocellular Carcinoma.. *Cancer informatics*. PMID: 37577174
3. Rare variants in IFFO1, DTNB, NLRC3 and SLC22A10 associate with Alzheimer's disease CSF profile of neuronal injury and inflammation.. *Molecular psychiatry*. PMID: 35173266
4. Nonhomologous end joining: new accessory factors fine tune the machinery.. *Trends in genetics : TIG*. PMID: 33785198
5. Developing a prognostic model of glutamine metabolism-related genes associated with clinical features and immune status in melanoma.. *Frontiers in oncology*. PMID: 40909968

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 30.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 37.9% |
| 有序区域 (pLDDT>70) 占比 | 44.4% |
| 可用 PDB 条目 | 6ABO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 44.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039008 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC4 | 0.994 | 0.975 | — |
| ALDH4A1 | 0.801 | 0.000 | — |
| XRCC5 | 0.641 | 0.287 | — |
| NHEJ1 | 0.567 | 0.292 | — |
| XRCC6 | 0.552 | 0.000 | — |
| IL23A | 0.535 | 0.535 | — |
| LIG4 | 0.531 | 0.287 | — |
| TCHP | 0.459 | 0.458 | — |
| MARCHF9 | 0.450 | 0.000 | — |
| GFAP | 0.428 | 0.428 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RNF183 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ACAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| XRCC4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| IL23A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SCML1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TLK2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DDHD1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| COBLL1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 6ABO | pLDDT=66.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Nucleus inner membr / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. IFFO1 — Non-homologous end joining factor IFFO1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小559 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0D2I5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010295-IFFO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IFFO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0D2I5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
