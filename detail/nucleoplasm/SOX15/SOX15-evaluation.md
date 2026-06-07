---
type: protein-evaluation
gene: "SOX15"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SOX15 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SOX15 / SOX27|SOX26 |
| 蛋白全称 | Transcription factor SOX-15 |
| 蛋白大小 | 233 aa |
| UniProt ID | O60248 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 233 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 74 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 10/10 | ×2 | **20** | 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX15/IF_images/A-431_HPA067196_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX15/IF_images/HaCaT_HPA067196_2.jpg|HaCaT]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 233 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 74 |

**评价**: PubMed 74 篇，中等研究热度

**关键文献**:
1. Ito M (2010). "Function and molecular evolution of mammalian Sox15, a singleton in the SoxG group of transcription factors". *Int J Biochem Cell Biol*. PMID: 19909824
2. Ogita Y et al. (2021). "Independent pseudogenizations and losses of sox15 during amniote diversification following asymmetric ohnolog evolution". *BMC Ecol Evol*. PMID: 34193037
3. Zhang M et al. (2019). "Inhibition of SOX15 Sensitizes Esophageal Squamous Carcinoma Cells to Paclitaxel". *Curr Mol Med*. PMID: 30950353
4. Choi EB et al. (2023). "Transcription factor SOX15 regulates stem cell pluripotency and promotes neural fate during differentiation by activating the neurogenic gene Hes5". *J Biol Chem*. PMID: 36764520
5. Wei B et al. (2022). "Sox15 Methylation Inhibits Cell Proliferation Through Wnt Signaling in Hepatocellular Carcinoma". *Front Oncol*. PMID: 35392235
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 233 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX15/SOX15-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | HMG_box_dom |
| InterPro | HMG_box_dom_sf |
| InterPro | SRY-related_HMG-box_TF-like |
| Pfam | HMG_box |
| SMART | HMG |
| PROSITE | HMG_BOX_2 |

**染色质调控潜力分析**: 染色质/DNA 结构域: hmg, hmg_box, hmg_box_2, hmg_box_dom, hmg_box_dom_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| CDH1 | 0 |  | no |
| CTNNB1 | 0 |  | no |
| POU5F1 | 0 |  | no |
| RBBP8NL | 0 |  | no |
| NANOG | 0 |  | no |
| NRSN2 | 0 |  | no |
| TM9SF4 | 0 |  | no |
| SOX4 | 0 |  | no |
| ENC1 | 0 |  | no |
| SALL4 | 0 |  | no |

**已知复合体成员** (GO-CC):

- C:chromatin (GO:0000785, ISA:NTNU_SB)
- C:transcription regulator complex (GO:0005667, IEA:Ensembl)
- F:chromatin binding (GO:0003682, IEA:Ensembl)
- P:chromatin organization (GO:0006325, NAS:UniProtKB)

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
多库结构域一致 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 74 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SOX15
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129194-SOX15
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SOX15%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O60248
- STRING: https://string-db.org/network/9606.ENSG00000129194
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60248


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[SOX15-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/SOX15/SOX15-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000129194-SOX15/subcellular

![](https://images.proteinatlas.org/67196/1244_D9_11_red_green.jpg)
![](https://images.proteinatlas.org/67196/1244_D9_14_red_green.jpg)
![](https://images.proteinatlas.org/67196/1247_D9_6_red_green.jpg)
![](https://images.proteinatlas.org/67196/1247_D9_8_red_green.jpg)
![](https://images.proteinatlas.org/67196/1573_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/67196/1573_A7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60248 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR050140; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129194-SOX15/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HOXB9 | Intact, Biogrid | true |
| BHLHE40 | Intact | false |
| C7orf50 | Biogrid | false |
| DAP3 | Biogrid | false |
| DDX24 | Biogrid | false |
| DDX50 | Biogrid | false |
| HSFY1 | Intact | false |
| HSFY2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
