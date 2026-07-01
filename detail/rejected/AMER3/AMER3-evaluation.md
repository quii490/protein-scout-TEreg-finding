---
type: protein-evaluation
gene: "AMER3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AMER3 -- 评估报告（REJECTED）

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | AMER3 |
| 评估日期 | 2026-06-03 |
| 数据状态 | harvest packet缺失 |

### 2. 拒绝原因

**核心原因: 数据不可用。AMER3 的harvest packet JSON文件在 protein_data/harvest_packets/ 目录中不存在，无法从自动化pipeline获取UniProt、AlphaFold、PubMed、STRING、IntAct、HPA等必需数据库信息。**


**备注**: AMER3 (APC membrane recruitment protein 3) 是AMER家族成员，与AMER2功能相似，参与Wnt信号通路调控。作为膜相关适配蛋白，预计定位于质膜/细胞质，核定位可能性低。


### 3. 数据获取状态

| 数据库 | 状态 | 说明 |
|---|---|---|
| UniProt | 不可用 | harvest packet缺失，无accession、序列长度、功能注释、亚细胞定位 |
| AlphaFold | 不可用 | harvest packet缺失，无pLDDT统计、PAE图像、PDB文件 |
| PubMed | 不可用 | harvest packet缺失，无文献计数、关键论文列表 |
| STRING | 不可用 | harvest packet缺失，无蛋白互作网络数据 |
| IntAct | 不可用 | harvest packet缺失，无实验验证互作记录 |
| HPA | 不可用 | harvest packet缺失，无免疫荧光定位、可靠性评分 |

### 4. 影响分析

缺乏harvest packet意味着无法进行以下六维核心评估:

| 评估维度 | 受影响的数据点 | 影响程度 |
|---|---|---|
| 核定位特异性 | HPA IF定位、UniProt Subcellular Location、GO Cellular Component | 完全无法评估 |
| 蛋白大小 | 氨基酸序列长度、分子量 | 完全无法评估 |
| 研究新颖性 | PubMed strict/broad文献计数 | 完全无法评估 |
| 三维结构 | AlphaFold pLDDT、PDB实验结构 | 完全无法评估 |
| 调控结构域 | InterPro/Pfam结构域注释 | 完全无法评估 |
| PPI网络 | STRING/IntAct/UniProt互作数据 | 完全无法评估 |

### 5. 可能原因分析

1. **基因名问题**: 基因符号可能不是当前HGNC官方符号，或存在别名未被识别
2. **数据库覆盖**: 该基因产物可能未被UniProt review（如TrEMBL条目），或为predicted protein
3. **Pipeline覆盖**: harvest pipeline可能未处理该基因（如批次遗漏、API限制）
4. **产物类型**: 该基因可能为假基因（pseudogene）、非编码RNA、或未充分注释的阅读框
5. **文件清理**: packet文件可能被误删除或移动到其他位置

### 6. 补救建议

1. 确认 AMER3 的当前HGNC官方符号，如有变更重新运行harvest
2. 手动检查 UniProt (https://www.uniprot.org) 和 GeneCards (https://www.genecards.org) 确认基因存在性
3. 如基因确实存在且有研究价值，手动创建harvest packet或使用交互式工具逐数据库查询
4. 如果确认该基因无数据库记录，将其标记为不适合当前研究目标
5. 对于已知功能定位于膜/胞质的基因（如AMER家族），可基于文献知识直接判定为不符合核蛋白标准

### 深度机制分析

**结构域架构**：AMER3（APC membrane recruitment protein 3/FAM123C）属于AMER（APC membrane recruitment）蛋白家族——该家族包含AMER1（WTX/FAM123A）、AMER2（FAM123B）和AMER3（FAM123C）。结构域架构基于家族保守性推断：N端为phosphatidylinositol-binding domain（PI-binding motif）——通过electrostatic interaction和疏水插入结合phosphatidylinositol (4,5)-bisphosphate（PI(4,5)P2）在质膜内叶（plasma membrane inner leaflet）——此PI-binding domain为AMER家族膜锚定的核心决定因子——中段为APC-binding domain——通过Armadillo repeat region识别adenomatous polyposis coli（APC）蛋白——C端含PDZ-binding motif（可能为-D/E-T/S-X-V/I/L-COOH）。APC是Wnt pathway β-catenin destruction complex的核心scaffold——AMER3通过APC-binding domain将APC招募至质膜——促进β-catenin destruction complex（Axin/GSK3β/CK1α/APC）在膜近端的组装——增强β-catenin phosphorylation（Ser33/Ser37/Thr41/Ser45 by CK1α and GSK3β）→β-TrCP recognition→K48 ubiquitination→proteasome degradation→Wnt pathway OFF state。

**PPI互作网络解读**：当前harvest packet缺失导致PPI数据完全不可用——STRING和IntAct数据无法获取。基于AMER1/WTX的已知PPI——WTX interactors包括APC、AXIN1、β-catenin（CTNNB1）、CRMP1（collapsin response mediator protein 1）、Scribble（SCRIB, cell polarity protein）——WTX-SCRIB interaction将Wnt pathway regulation与apical-basal cell polarity耦合。如AMER3保留类似PPI网络——其膜锚定-APC recruitment功能将整合cell adhesion/cell polarity signal与Wnt pathway activity。

**结构解读**：harvest packet缺失导致AlphaFold pLDDT数据和PDB结构数据不可用。基于AMER1已知结构信息——WTX的PI(4,5)P2-binding domain（N-terminal ~200 aa）为predicted disordered region——通过electrostatic interaction（basic residue clustering: Lys/Arg-rich patches）结合酸性phospholipid——无明确定义的三级结构fold。APC-binding domain（central ~500 aa）可能形成extended coiled-coil或solenoid fold——提供长程的multiple APC-interaction interface。

**TE调控展望**：AMER家族蛋白的TE调控关联主要通过APC-β-catenin-Wnt pathway轴间接实现。APC通过β-catenin nuclear translocation调控TCF/LEF-dependent transcription——TCF/LEF consensus motif（5'-CTTTGA/TA-3'）与多种retrotransposon LTR中的enhancer element有显著序列同源性——AMER3-mediated Wnt pathway suppression可能间接抑制TCF/LEF-driven TE transcription。WTX（AMER1）已知具有nuclear pool——参与β-catenin nuclear export——但AMER3是否具有类似核功能完全未知。当前数据缺失状态无法完成有意义的机制分析——等待harvest packet重新生成后进行完整六维评估和深度机制分析。

### 7. 评估结论

AMER3 因harvest packet数据缺失，无法完成标准六维蛋白评估。在获得完整数据之前，**维持拒绝状态**。如后续补充packet数据或确认该基因的数据库记录状态，可重新进行完整评估。

![[Projects/TEreg-finding/protein-interested/detail/rejected/AMER3/AMER3-PAE.png]]
